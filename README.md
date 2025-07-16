Gemma IA Offline - Versión Normal (1.2.5) y Lite (1.2.6)
Gemma IA Offline es un programa diseñado para proporcionar asistencia en emergencias sin conexión a internet, utilizando los modelos de peso abierto (open-weight) Gemma de Google. Ofrece dos versiones:

Versión Normal (1.2.5): Utiliza el modelo gemma3:latest (9B parámetros, ~4-5 GB VRAM), ideal para PCs con GPU dedicada (por ejemplo, RTX 5060) y al menos 8 GB RAM. Soporta la creación de archivos .txt, .pdf, y .html con guías de supervivencia, resúmenes, y respuestas basadas en ubicación simulada.
Versión Lite (1.2.6): Utiliza el modelo gemma2:2b (2B parámetros, ~1-2 GB VRAM), optimizada para PCs de gama baja (CPU de doble núcleo, 4-8 GB RAM, sin GPU dedicada). Solo soporta archivos .txt para minimizar el uso de recursos.

Ambas versiones funcionan offline tras la configuración inicial y generan archivos en la carpeta GemmaFiles, que se abre automáticamente la primera vez que se crea un archivo.
Características

Interfaz de chat:
Mensajes del usuario en burbujas rojas (derecha).
Respuestas de Gemma en burbujas grises (izquierda, versión Normal) o grises (Lite).


Consultas de emergencia:
Ejemplo: "¿Cómo sobrevivir a un terremoto?" genera un documento .txt (y .pdf/.html en la versión Normal).
Ejemplo: "¿Dónde estoy si estoy en un bosque cerca de Madrid?" proporciona consejos basados en la ubicación.


Creación de documentos:
Palabras clave como "crea", "haz", "hazme" generan archivos .txt (y .pdf/.html en la versión Normal).
Ejemplo: "Hazme un resumen sobre primeros auxilios" crea un archivo en GemmaFiles.


Ubicación simulada:
Usa GemmaFiles/location.txt o extrae la ubicación de la consulta (por ejemplo, "en un bosque cerca de Madrid").


Soporte offline:
Tras la configuración inicial (requiere internet), funciona sin conexión.



Requisitos previos
Versión Normal (1.2.5)

Sistema operativo: Windows 10/11.
Hardware: CPU/GPU con ~4-5 GB VRAM (por ejemplo, RTX 5060), 8 GB RAM.
Internet: Solo para la configuración inicial (descarga de Python, Ollama, modelo gemma3:latest).
Permisos: Ejecutar como administrador.

Versión Lite (1.2.6)

Sistema operativo: Windows 10/11.
Hardware: CPU de doble núcleo, 4 GB RAM, ~1-2 GB VRAM (o sin GPU).
Internet: Solo para la configuración inicial (descarga de Python, Ollama, modelo gemma2:2b).
Permisos: Ejecutar como administrador.

Instalación

Descarga el proyecto:

Clona este repositorio o descarga el zip desde GitHub.
Estructura del repositorio:gemma_ia_offline/
├── gemma_emergency_chat(4).py
├── index(1).html
├── requirements.txt
├── LICENSE
├── README.md
└── GemmaFiles/
    └── location.txt




Instala dependencias:

Abre una consola (cmd) en la carpeta del proyecto.
Ejecuta:pip install -r requirements.txt


Nota: La versión Normal requiere PyPDF2 y beautifulsoup4 además de ollama. La versión Lite solo requiere ollama.


Descarga el modelo Gemma:

Acepta los términos de uso en Hugging Face:
Versión Normal: gemma3:latest
Versión Lite: gemma2:2b


Descarga el modelo con Ollama:ollama pull gemma3:latest  # Versión Normal
ollama pull gemma2:2b      # Versión Lite




Ejecuta el programa:

En la consola, ejecuta:python gemma_emergency_chat(4).py


El navegador se abrirá en http://localhost:8000.



Uso

Accede a la interfaz:

En http://localhost:8000, verás una interfaz de chat con:
Título: "Gemma IA Offline - Versión 1.2.5" (Normal) o "Gemma IA Offline Lite - Versión 1.2.6" (Lite).
Instrucciones con ejemplos.
Área de chat (burbujas rojas para el usuario, grises para Gemma).
Campo de texto y botón "Enviar" en la parte inferior.
Botón "Salir" en la parte superior derecha.




Consultas de ejemplo:

Ubicación: "¿Dónde estoy si estoy en un bosque cerca de Madrid?"
Supervivencia: "Hazme un documento sobre cómo sobrevivir a un terremoto"
Resumen: "Hazme un resumen sobre primeros auxilios"
Consulta libre: "¿Cómo realizar RCP?"
Salir: Escribe "salir" o haz clic en "Salir".


Archivos generados:

Se guardan en GemmaFiles (por ejemplo, gemma_ia_offline/GemmaFiles/2025-07-16_documento_supervivir_terremoto.txt).
La carpeta se abre automáticamente la primera vez que generes un archivo.
La versión Normal también genera .pdf y .html (si están configurados).


Configurar ubicación (opcional):

Edita GemmaFiles/location.txt, por ejemplo:Bosque cerca de Madrid, España





Creación del ejecutable

Instala PyInstaller:
pip install pyinstaller


Crea el ejecutable:

Para la versión Normal:pyinstaller --noconfirm --onefile --add-data "index(1).html;." --add-data "requirements.txt;." --add-data "README.md;." --add-data "GemmaFiles;GemmaFiles" --name GemmaIAOffline gemma_emergency_chat(4).py


Para la versión Lite:pyinstaller --noconfirm --onefile --add-data "index(1).html;." --add-data "requirements.txt;." --add-data "README.md;." --add-data "GemmaFiles;GemmaFiles" --name GemmaIAOfflineLite gemma_emergency_chat(4).py




Distribución:

Copia el ejecutable (GemmaIAOffline.exe o GemmaIAOfflineLite.exe) desde dist/ a la carpeta del proyecto.
Asegúrate de incluir la subcarpeta GemmaFiles.



Cumplimiento normativo
Este proyecto utiliza los modelos Gemma de Google, que cumplen con las políticas de seguridad de Google (filtrado de PII, evaluaciones de seguridad). Los usuarios son responsables de cumplir con las regulaciones locales, como el EU AI Act, y de no usar el programa para actividades ilegales o para generar contenido dañino. Consulta las model cards de Gemma para más detalles:

Versión Normal: gemma3:latest
Versión Lite: gemma2:2b

Política de uso
Está estrictamente prohibido usar Gemma IA Offline para actividades ilegales, generar contenido dañino, o violar los términos de uso de Google para los modelos Gemma (ver https://ai.google.dev/gemma/terms).
Advertencia sobre propiedad intelectual
El contenido generado por Gemma IA Offline (usando los modelos Gemma de Google) es responsabilidad del usuario. Asegúrate de no usar el contenido generado para infringir derechos de autor o propiedad intelectual.
Descargo de responsabilidad
La información en este proyecto es solo para fines informativos y no constituye asesoramiento legal. Consulta a un abogado para cuestiones legales relacionadas con el uso de este software.
Solución de problemas

Permisos denegados: Ejecuta el programa o ejecutable como administrador.
No se conecta al servidor: Asegúrate de que el programa esté corriendo y accede a http://localhost:8000.
Error de memoria: Cierra otras aplicaciones. La versión Lite usa ~1-2 GB VRAM, la Normal ~4-5 GB.
Configuración lenta: La primera ejecución requiere internet para descargar Python, Ollama, y el modelo.
Archivos no encontrados: Verifica que GemmaFiles esté en la carpeta del proyecto.

Contribuciones
¡Las contribuciones son bienvenidas! Por favor, revisa el archivo LICENSE (MIT) y crea un pull request con tus cambios. Asegúrate de no incluir los pesos de los modelos Gemma en el repositorio.
Licencia
El código fuente de este proyecto está licenciado bajo la Licencia MIT (ver el archivo LICENSE). Los modelos Gemma (gemma3:latest y gemma2:2b) están sujetos a la licencia de Google, que debes aceptar en Hugging Face antes de usarlos:

Versión Normal: https://huggingface.co/google/gemma-7b
Versión Lite: https://huggingface.co/google/gemma-2b

Agradecimientos

Google DeepMind por los modelos Gemma.
Hugging Face y Ollama por facilitar el acceso a los modelos.
Comunidad de código abierto por las herramientas y bibliotecas utilizadas.
