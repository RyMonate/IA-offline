Gemma IA Offline
Gemma IA Offline is an essential offline AI tool designed for emergency preparedness, offering survival guidance and document creation in crisis situations. Ideal for remote areas, disaster response, or low-resource environments, it supports multiple languages and comes in two variants: a feature-rich version for capable PCs and a lightweight version for low-end devices.
Naming Disclaimer
Gemma IA Offline is an independent, open-source project that utilizes Google’s Gemma AI models. It is not affiliated with, endorsed by, or developed by Google. The name "Gemma" refers to the AI models powering the application, licensed under Google’s terms.
Installation and Setup

Download:

Clone the repository or download the zip file from GitHub.

Unzip to C:\Users\<YourUsername>\Downloads\gemma-ia-offline.

Ensure the folder structure is:
gemma-ia-offline/
├── src/
│   ├── normal/
│   │   ├── GemmaIAOffline.exe
│   │   ├── gemma_emergency_chat_v1.3.py
│   │   ├── index_v1.3.html
│   │   └── requirements.txt
│   └── lite/
│       ├── GemmaIAOfflineLite.exe
│       ├── gemma_emergency_chat_v1.3.py
│       ├── index_v1.3.html
│       └── requirements.txt
├── GemmaFiles/
│   ├── location.txt
│   ├── config.json
├── assets/
├── LICENSE
├── README.md
└── CHANGELOG.md




Run the Program:

Normal Version (for PCs with GPU and 8 GB RAM):
Navigate to C:\Users\<YourUsername>\Downloads\gemma-ia-offline\src\normal.
Double-click GemmaIAOffline.exe.


Lite Version (for low-end PCs with 4-8 GB RAM, no GPU):
Navigate to C:\Users\<YourUsername>\Downloads\gemma-ia-offline\src\lite.
Double-click GemmaIAOfflineLite.exe.


On first run, the program will automatically set up dependencies and download the required model. This requires an internet connection and may take a few minutes.
A progress bar will appear during setup, followed by your browser opening to a chat interface.



Usage

Select your language (English, Spanish, or Russian) from the dropdown and click “Apply Language.”
Enter emergency queries (e.g., “How to survive a flood?”) and click “Submit” or press Enter.
Use keywords like “create,” “make,” “generate” (English), “crear,” “hacer,” “generar” (Spanish), or “создать,” “сделать,” “генерировать” (Russian) to save files in GemmaFiles.
Click “Open GemmaFiles” to view saved files or type “exit” to close the program.

Troubleshooting

Permission Denied: Right-click the .exe and select “Run as administrator.”
Model Download Fails: Ensure an internet connection. Check disk space (~5 GB for Normal, ~2 GB for Lite) and restart the .exe.
Browser Not Opening: Manually open http://localhost:8000. If it fails, restart the .exe.
Slow Startup: Wait for the progress bar to complete on first run.
Files Not Found: Verify the GemmaFiles folder exists in C:\Users\<YourUsername>\Downloads\gemma-ia-offline with location.txt and config.json.

Contributions
Contributions are welcome! Review the LICENSE (MIT) and submit pull requests. Do not include model weights.
License
Source code: MIT License (see LICENSE). Gemma models are licensed under Google’s terms, available at https://ai.google.dev/gemma/terms.
Acknowledgments

Google DeepMind for Gemma models.
Open-source community for tools and libraries.
