import os
import re
import json
import subprocess
import sys
import urllib.request
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import ollama

# Versión del programa
VERSION = "1.2.6"

# Carpeta para almacenar archivos
if getattr(sys, 'frozen', False):
    BASE_PATH = sys._MEIPASS
else:
    BASE_PATH = os.path.dirname(__file__)
FOLDER_PATH = os.path.join(BASE_PATH, "GemmaFiles")

# Bandera para abrir la carpeta solo la primera vez
FIRST_FILE_SAVED = False

def setup_environment():
    """Configura el entorno: instala Python, Ollama y modelo."""
    print("Configurando el entorno...")

    # Verifica si Python está instalado
    try:
        subprocess.run(["python", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Python no está instalado. Descargando e instalando Python 3.10...")
        python_installer_url = "https://www.python.org/ftp/python/3.10.11/python-3.10.11-amd64.exe"
        python_installer_path = os.path.join(BASE_PATH, "python-installer.exe")
        try:
            urllib.request.urlretrieve(python_installer_url, python_installer_path)
            subprocess.run([python_installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
            os.remove(python_installer_path)
            print("Python instalado correctamente.")
        except Exception as e:
            print(f"Error al instalar Python: {str(e)}")
            sys.exit(1)

    # Instala la dependencia ollama
    try:
        subprocess.run(["pip", "install", "ollama==0.3.3"], check=True)
        print("Dependencia ollama instalada correctamente.")
    except subprocess.CalledProcessError:
        print("Error al instalar ollama. Asegúrate de tener pip configurado.")
        sys.exit(1)

    # Verifica si Ollama está instalado
    ollama_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Programs", "Ollama", "ollama.exe")
    if not os.path.exists(ollama_path):
        print("Ollama no está instalado. Descargando e instalando Ollama...")
        ollama_installer_url = "https://ollama.com/download/OllamaSetup.exe"
        ollama_installer_path = os.path.join(BASE_PATH, "ollama-installer.exe")
        try:
            urllib.request.urlretrieve(ollama_installer_url, ollama_installer_path)
            subprocess.run([ollama_installer_path, "/S"], check=True)
            os.remove(ollama_installer_path)
            print("Ollama instalado correctamente.")
        except Exception as e:
            print(f"Error al instalar Ollama: {str(e)}")
            sys.exit(1)

    # Verifica si el modelo gemma2:2b está descargado
    try:
        result = subprocess.run(["ollama", "list"], capture_output=True, text=True, check=True)
        if "gemma2:2b" not in result.stdout:
            print("Descargando el modelo gemma2:2b...")
            subprocess.run(["ollama", "pull", "gemma2:2b"], check=True)
            print("Modelo gemma2:2b descargado correctamente.")
    except subprocess.CalledProcessError:
        print("Error al verificar o descargar el modelo gemma2:2b.")
        sys.exit(1)

def setup_folder():
    """Crea la carpeta GemmaFiles si no existe."""
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)

def get_simulated_location(query):
    """Simula la obtención de la ubicación desde un archivo o la consulta."""
    location_file = os.path.join(FOLDER_PATH, "location.txt")
    if os.path.exists(location_file):
        try:
            with open(location_file, "r", encoding="utf-8") as f:
                location = f.read().strip()
                return location if location else "Ubicación desconocida"
        except Exception:
            return "Ubicación desconocida"
    
    query_lower = query.lower()
    if any(keyword in query_lower for keyword in ["dónde estoy", "ubicación", "perdido"]):
        match = re.search(r"(?:en|cerca de|en un|en una)\s+([^\?\.]+)", query_lower)
        if match:
            return match.group(1).strip().capitalize()
    return "Ubicación desconocida"

def needs_file_creation(query):
    """Determina si la consulta requiere crear un archivo."""
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ["crea", "haz", "hazme"])

def is_summary(query):
    """Determina si la consulta es para un resumen (.txt)."""
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ["resumen", "resume", "summarize"])

def is_info_document(query):
    """Determina si la consulta es para un documento informativo (.txt)."""
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ["documento", "información", "sobre"])

def is_location_query(query):
    """Determina si la consulta está relacionada con la ubicación."""
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ["dónde estoy", "ubicación", "perdido"])

def is_survival_query(query):
    """Determina si la consulta está relacionada con supervivencia."""
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in ["supervivencia", "sobrevivir", "emergencia", "terremoto", "inundación", "incendio", "bosque", "montaña", "primeros auxilios", "rcp", "herida", "quemadura", "evacuación", "desastre"])

def get_file_name_suffix(query):
    """Genera un sufijo para el nombre del archivo basado en el tema de la consulta."""
    keywords = ["crea", "haz", "hazme", "resumen", "resume", "summarize", "documento", "información", "sobre", "dónde estoy", "ubicación", "perdido", "supervivencia", "sobrevivir", "emergencia", "terremoto", "inundación", "incendio", "bosque", "montaña", "primeros auxilios", "rcp", "herida", "quemadura", "evacuación", "desastre"]
    suffix = query.lower()
    for keyword in keywords:
        suffix = suffix.replace(keyword, "")
    suffix = re.sub(r'[^\w\s]', '', suffix).strip()
    suffix = suffix.replace(" ", "_")[:50]
    return suffix if suffix else "generico"

def get_unique_file_path(file_path):
    """Genera un nombre de archivo único añadiendo un sufijo numérico si es necesario."""
    base, ext = os.path.splitext(file_path)
    counter = 1
    new_file_path = file_path
    while os.path.exists(new_file_path):
        new_file_path = f"{base}_{counter}{ext}"
        counter += 1
    return new_file_path

def format_response(text):
    """Convierte *texto* en negrita y preserva listas."""
    text = re.sub(r'\*([^\s*][^*]*[^\s*])\*', r'<strong>\1</strong>', text)
    lines = text.split('\n')
    formatted_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('* '):
            formatted_lines.append(f"→ {stripped_line[2:]}")
        else:
            formatted_lines.append(line)
    return '\n'.join(formatted_lines)

def save_txt(content, query, prefix="documento"):
    """Guarda un archivo .txt con fecha y nombre basado en el tema."""
    global FIRST_FILE_SAVED
    date = datetime.now().strftime("%Y-%m-%d")
    suffix = get_file_name_suffix(query)
    file_name = f"{date}_{prefix}_{suffix}.txt"
    file_path = os.path.join(FOLDER_PATH, file_name)
    file_path = get_unique_file_path(file_path)
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"Contenido generado para: {query}\n\n{content}")
        if not FIRST_FILE_SAVED:
            try:
                os.startfile(FOLDER_PATH)  # Abre la carpeta GemmaFiles en el Explorador de Windows
                FIRST_FILE_SAVED = True
            except Exception:
                pass
        return f"Archivo guardado en {file_path}\nCarpeta: {FOLDER_PATH}"
    except Exception as e:
        return f"Error al guardar el archivo: {str(e)}\nCarpeta: {FOLDER_PATH}"

class GemmaRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index(1).html":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open(os.path.join(BASE_PATH, "index(1).html"), "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            except FileNotFoundError:
                self.send_response(404)
                self.end_headers()
                self.wfile.write("Error: index(1).html no encontrado.".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("404 Not Found".encode("utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        params = parse_qs(post_data)
        user_input = params.get("query", [""])[0]
        
        response_data = {"status": "success", "message": "", "title": "Gemma IA Offline Lite"}
        conversation = []

        if user_input.lower() == "salir":
            response_data["message"] = "¡Hasta luego! Cierra la ventana para terminar."
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode("utf-8"))
            return

        if is_location_query(user_input):
            location = get_simulated_location(user_input)
            prompt = f"El usuario está en la siguiente ubicación: {location}. Proporciona consejos prácticos para encontrar ayuda, refugio o recursos en esta área si está perdido o en una emergencia."
            conversation.append({"role": "user", "content": prompt})
            
            try:
                response = ollama.chat(model="gemma2:2b", messages=conversation)
                location_advice = response["message"]["content"]
                formatted_advice = format_response(location_advice)
                conversation.append({"role": "assistant", "content": location_advice})
                response_data["message"] = formatted_advice
                response_data["title"] = "Gemma IA Offline Lite (Consejos de Ubicación)"
            except Exception as e:
                response_data["status"] = "error"
                response_data["message"] = f"Error: No se pudo procesar la solicitud. Asegúrate de que Ollama esté corriendo y que el modelo 'gemma2:2b' esté instalado. Detalle: {str(e)}"
        
        elif needs_file_creation(user_input):
            query = user_input
            if is_summary(user_input):
                content_to_process = user_input.replace("crea", "").replace("haz", "").replace("hazme", "").replace("resumen de", "").replace("resume", "").replace("summarize", "").strip()
                query = f"Por favor, crea un resumen del siguiente contenido:\n{content_to_process}"
                prefix = "resumen"
            else:
                content_to_process = user_input.replace("crea", "").replace("haz", "").replace("hazme", "").replace("documento", "").replace("información", "").replace("sobre", "").strip()
                query = f"Genera un documento informativo sobre el siguiente tema de emergencia:\n{content_to_process}"
                prefix = "documento"
                
            conversation.append({"role": "user", "content": query})
            
            try:
                response = ollama.chat(model="gemma2:2b", messages=conversation)
                document_content = response["message"]["content"]
                formatted_content = format_response(document_content)
                save_result = save_txt(document_content, user_input, prefix=prefix)
                response_data["message"] = f"{formatted_content}\n\n{save_result}"
                response_data["title"] = f"Gemma IA Offline Lite ({'Resumen' if prefix == 'resumen' else 'Documento'})"
                conversation.append({"role": "assistant", "content": document_content})
            except Exception as e:
                response_data["status"] = "error"
                response_data["message"] = f"Error: No se pudo procesar la solicitud. Asegúrate de que Ollama esté corriendo y que el modelo 'gemma2:2b' esté instalado. Detalle: {str(e)}"
        
        else:
            query = user_input
            if is_survival_query(user_input):
                location = get_simulated_location(user_input)
                prompt = f"Proporciona información detallada sobre cómo sobrevivir en la siguiente situación: {user_input}. Si es relevante, considera que el usuario está en esta ubicación: {location}."
            else:
                prompt = user_input
            conversation.append({"role": "user", "content": prompt})
            
            try:
                response = ollama.chat(model="gemma2:2b", messages=conversation)
                assistant_response = response["message"]["content"]
                formatted_response = format_response(assistant_response)
                response_data["message"] = formatted_response
                conversation.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                response_data["status"] = "error"
                response_data["message"] = f"Error: No se pudo procesar la solicitud. Asegúrate de que Ollama esté corriendo y que el modelo 'gemma2:2b' esté instalado. Detalle: {str(e)}"

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode("utf-8"))

def run_server():
    setup_folder()
    setup_environment()
    try:
        result = subprocess.run(["tasklist"], capture_output=True, text=True, check=True)
        if "ollama.exe" not in result.stdout:
            print("Iniciando el servidor Ollama...")
            subprocess.Popen(["ollama", "serve"], creationflags=subprocess.CREATE_NO_WINDOW)
    except subprocess.CalledProcessError:
        print("Error al verificar el estado de Ollama.")
        sys.exit(1)

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, GemmaRequestHandler)
    print("Servidor iniciado en http://localhost:8000")
    import webbrowser
    webbrowser.open("http://localhost:8000")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print("Servidor detenido.")

if __name__ == "__main__":
    run_server()
