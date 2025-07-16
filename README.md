Gemma IA Offline - Normal (1.2.5) and Lite (1.2.6) Versions
Gemma IA Offline is a program designed to provide emergency assistance without an internet connection, leveraging Google’s open-weight Gemma models. It offers two versions:

Normal Version (1.2.5): Uses the gemma3:latest model (9B parameters, ~4-5 GB VRAM), ideal for PCs with a dedicated GPU (e.g., RTX 5060) and at least 8 GB RAM. Supports generating .txt, .pdf, and .html files for survival guides, summaries, and location-based responses.
Lite Version (1.2.6): Uses the gemma2:2b model (2B parameters, ~1-2 GB VRAM), optimized for low-end PCs (dual-core CPU, 4-8 GB RAM, no dedicated GPU). Supports only .txt files to minimize resource usage.

Both versions operate offline after initial setup and save generated files in the GemmaFiles folder, which automatically opens the first time a file is created.
Features

Chat Interface:
User messages appear in red bubbles (right side).
Gemma’s responses appear in gray bubbles (left side, both versions).


Emergency Queries:
Example: "How to survive an earthquake?" generates a .txt file (and .pdf/.html in Normal version).
Example: "Where am I if I’m in a forest near Madrid?" provides location-based advice.


Document Creation:
Keywords like "create," "make," or "generate" trigger file generation (.txt in both versions; .pdf/.html in Normal).
Example: "Generate a summary about first aid" creates a file in GemmaFiles.


Simulated Location:
Uses GemmaFiles/location.txt or extracts location from queries (e.g., "in a forest near Madrid").


Offline Support:
Works without internet after initial setup (requires internet for first-time configuration).



Prerequisites
Normal Version (1.2.5)

Operating System: Windows 10/11.
Hardware: CPU/GPU with ~4-5 GB VRAM (e.g., RTX 5060), 8 GB RAM.
Internet: Required only for initial setup (downloads Python, Ollama, gemma3:latest model).
Permissions: Run as administrator.

Lite Version (1.2.6)

Operating System: Windows 10/11.
Hardware: Dual-core CPU, 4 GB RAM, ~1-2 GB VRAM (or no GPU).
Internet: Required only for initial setup (downloads Python, Ollama, gemma2:2b model).
Permissions: Run as administrator.

Installation

Download the Project:

Clone this repository or download the zip from GitHub.
Repository structure:gemma_ia_offline/
├── gemma_emergency_chat(4).py
├── index(1).html
├── requirements.txt
├── LICENSE
├── README.md
└── GemmaFiles/
    └── location.txt




Install Dependencies:

Open a command prompt (cmd) in the project folder.
Run:pip install -r requirements.txt


Note: The Normal version requires PyPDF2 and beautifulsoup4 in addition to ollama. The Lite version requires only ollama.


Download the Gemma Model:

Accept the terms of use on Hugging Face:
Normal Version: gemma3:latest
Lite Version: gemma2:2b


Download the model using Ollama:ollama pull gemma3:latest  # Normal Version
ollama pull gemma2:2b      # Lite Version




Run the Program:

In the command prompt, execute:python gemma_emergency_chat(4).py


The browser will open at http://localhost:8000.



Usage

Access the Interface:

At http://localhost:8000, you’ll see a chat interface with:
Title: "Gemma IA Offline - Version 1.2.5" (Normal) or "Gemma IA Offline Lite - Version 1.2.6" (Lite).
Instructions with example queries.
Chat area (user messages in red bubbles on the right, Gemma responses in gray bubbles on the left).
Text input field and "Submit" button at the bottom.
"Exit" button at the top right.




Example Queries:

Location: "Where am I if I’m in a forest near Madrid?"
Survival: "Generate a document about how to survive an earthquake"
Summary: "Generate a summary about first aid"
General Query: "How to perform CPR?"
Exit: Type "exit" or click the "Exit" button.


Generated Files:

Saved in GemmaFiles (e.g., gemma_ia_offline/GemmaFiles/2025-07-16_document_earthquake_survival.txt).
The GemmaFiles folder opens automatically the first time a file is generated.
The Normal version also generates .pdf and .html files (if configured).


Configure Location (Optional):

Edit GemmaFiles/location.txt, e.g.:Forest near Madrid, Spain


Alternatively, include the location in queries (e.g., "Where am I if I’m in a forest near Madrid?").



Building the Executable

Install PyInstaller:
pip install pyinstaller


Create the Executable:

For the Normal version:pyinstaller --noconfirm --onefile --add-data "index(1).html;." --add-data "requirements.txt;." --add-data "README.md;." --add-data "GemmaFiles;GemmaFiles" --name GemmaIAOffline gemma_emergency_chat(4).py


For the Lite version:pyinstaller --noconfirm --onefile --add-data "index(1).html;." --add-data "requirements.txt;." --add-data "README.md;." --add-data "GemmaFiles;GemmaFiles" --name GemmaIAOfflineLite gemma_emergency_chat(4).py




Distribution:

Copy the executable (GemmaIAOffline.exe or GemmaIAOfflineLite.exe) from dist/ to the project folder.
Ensure the GemmaFiles subfolder is included.



Regulatory Compliance
This project uses Google’s Gemma models, which adhere to Google’s safety policies (PII filtering, safety evaluations). Users are responsible for complying with local regulations, such as the EU AI Act, and must not use the program for illegal activities or to generate harmful content. Refer to the Gemma model cards for details:

Normal Version: gemma3:latest
Lite Version: gemma2:2b

Usage Policy
Using Gemma IA Offline for illegal activities, generating harmful content, or violating Google’s terms of use for the Gemma models is strictly prohibited (see https://ai.google.dev/gemma/terms).
Intellectual Property Notice
Content generated by Gemma IA Offline (using Google’s Gemma models) is the user’s responsibility. Ensure that generated content does not infringe on copyrights or intellectual property rights.
Disclaimer
The information in this project is for informational purposes only and does not constitute legal advice. Consult a lawyer for legal questions related to the use of this software.
Troubleshooting

Permission Denied: Run the program or executable as administrator.
Cannot Connect to Server: Ensure the program is running and access http://localhost:8000.
Memory Errors: Close other applications. The Lite version uses ~1-2 GB VRAM, Normal uses ~4-5 GB.
Slow Setup: Initial setup requires internet for downloading Python, Ollama, and the model.
Files Not Found: Check that files are saved in gemma_ia_offline/GemmaFiles. The folder should open automatically the first time.

Contributions
Contributions are welcome! Please review the LICENSE file (MIT) and submit a pull request with your changes. Do not include Gemma model weights in the repository.
License
The source code of this project is licensed under the MIT License (see the LICENSE file). The Gemma models (gemma3:latest and gemma2:2b) are subject to Google’s license, which you must accept on Hugging Face before use:

Normal Version: https://huggingface.co/google/gemma-7b
Lite Version: https://huggingface.co/google/gemma-2b

Acknowledgments

Google DeepMind for the Gemma models.
Hugging Face and Ollama for facilitating model access.
Open-source community for the tools and libraries used.
