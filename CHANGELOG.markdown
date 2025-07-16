# Changelog

All notable changes to Gemma IA Offline will be documented in this file.

## [1.3] - 2025-07-16
### Added
- **Lite Version (1.3)**:
  - Multilingual support: English, Spanish, Russian via UI dropdown and `GemmaFiles/config.json`.
  - Customizable UI colors: Change user and AI bubble colors via UI or `GemmaFiles/config.json`.
  - “Open GemmaFiles” button: Opens `GemmaFiles` folder in File Explorer from the UI.
  - Offline knowledge base: Preloaded emergency guides in `GemmaFiles/kb/emergencies.json` (e.g., earthquake, flood, first aid).
  - Startup progress bar: Tkinter-based progress bar during executable launch (model loading, server setup).
- **Assets**: Added `icon-lite.ico` (chat bubble with red dot, slashed Wi-Fi) for the Lite executable.

### Changed
- Updated `gemma_emergency_chat.py` and `index.html` to support new features.
- Added `tkinter` to `requirements.txt` (included with Python).
- Improved `README.md` with instructions for new features and compliance notes.

### Fixed
- Enhanced error handling for low-memory scenarios and missing `GemmaFiles` subfolders.

## [1.2.6] - 2025-07-16
### Added
- **Lite Version (1.2.6)**:
  - Introduced lightweight version with `gemma2:2b` model (~1-2 GB VRAM).
  - Simplified chat interface with minimal CSS (no Tailwind).
  - Reduced dependencies to `ollama` only.
  - `.txt` file generation only.
- **Normal Version (1.2.6)**:
  - Improved file handling in `GemmaFiles` with auto-open on first creation.

### Changed
- Updated `README.md` for clarity and EU AI Act compliance.
- Restructured repository with `src/normal` and `src/lite`.

### Fixed
- Fixed file save path issues.

## [1.2.5] - 2025-07-01
- Initial release of Normal version with `gemma3:latest` model.
- Supported `.txt`, `.pdf`, `.html` file generation.
- Chat interface with Tailwind CSS.
- Simulated location via `GemmaFiles/location.txt`.
- Offline operation after setup.