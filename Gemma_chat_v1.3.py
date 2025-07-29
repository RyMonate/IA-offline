import http.server
import socketserver
import json
import os
import webbrowser
import ollama
import threading
import tkinter as tk
from tkinter import ttk
import time
from datetime import datetime
from PyPDF2 import PdfWriter
from bs4 import BeautifulSoup

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GEMMA_FILES = os.path.join(os.path.dirname(BASE_DIR), "..", "GemmaFiles")
CONFIG_FILE = os.path.join(GEMMA_FILES, "config.json")

# Ensure GemmaFiles exists
os.makedirs(GEMMA_FILES, exist_ok=True)

# Load or create config
def load_config():
    default_config = {"language": "en"}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                pass
    with open(CONFIG_FILE, "w") as f:
        json.dump(default_config, f, indent=4)
    return default_config

# Save config
def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

# Progress bar for executable startup
def show_progress_bar():
    root = tk.Tk()
    root.title("Gemma IA Offline - Loading")
    root.geometry("250x80")
    progress = ttk.Progressbar(root, length=200, mode="determinate")
    progress.pack(pady=10)
    label = tk.Label(root, text="Loading...")
    label.pack()
    
    def update_progress():
        steps = ["Initializing", "Loading model", "Starting server", "Ready"]
        for i in range(101):
            progress["value"] = i
            label.config(text=f"{steps[min(i // 25, 3)]}... {i}%")
            root.update()
            time.sleep(0.05)
        root.destroy()
    
    threading.Thread(target=update_progress, daemon=True).start()
    root.mainloop()

# Start progress bar if executable
if hasattr(sys, 'frozen'):
    show_progress_bar()

# HTTP request handler
class ChatHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "index_v1.3.html"
        return super().do_GET()
    
    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length).decode("utf-8")
        data = json.loads(post_data)
        
        action = data.get("action")
        config = load_config()  # Reload config for each request
        
        if action == "chat":
            user_message = data.get("message", "")
            language = config.get("language", "en")
            response = process_message(user_message, language)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"response": response}).encode("utf-8"))
        
        elif action == "update_config":
            config.update(data.get("config", {}))
            save_config(config)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
        
        elif action == "open_folder":
            os.startfile(GEMMA_FILES)
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))

# Process user message
def process_message(message, language):
    if message.lower() == "exit":
        os._exit(0)
    
    lang_map = {"en": "English", "es": "Spanish", "ru": "Russian"}
    prompt = f"Answer in {lang_map.get(language, 'English')}: {message}"
    try:
        response = ollama.chat(model="gemma3:latest", messages=[{"role": "user", "content": prompt}])["message"]["content"]
    except Exception as e:
        response = f"Error: {str(e)}"
    
    # Save to files if requested (English, Spanish, Russian keywords)
    create_keywords = ["create", "make", "generate", "crear", "hacer", "generar", "создать", "сделать", "генерировать"]
    if any(keyword in message.lower() for keyword in create_keywords):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        # Text file
        txt_file = os.path.join(GEMMA_FILES, f"{timestamp}_response.txt")
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(response)
        # PDF file
        pdf_file = os.path.join(GEMMA_FILES, f"{timestamp}_response.pdf")
        pdf = PdfWriter()
        pdf.add_page(PdfWriter().add_blank_page(width=595, height=842))
        with open(pdf_file, "wb") as f:
            pdf.write(f)
        # HTML file
        html_file = os.path.join(GEMMA_FILES, f"{timestamp}_response.html")
        soup = BeautifulSoup("<html><body><p>" + response + "</p></body></html>", "html.parser")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(str(soup))
        # Auto-open GemmaFiles on first file creation
        if not hasattr(process_message, "folder_opened"):
            os.startfile(GEMMA_FILES)
            process_message.folder_opened = True
    
    return response

# Start server
PORT = 8000
with socketserver.TCPServer(("", PORT), ChatHandler) as httpd:
    print(f"Server running at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}")
    httpd.serve_forever()
