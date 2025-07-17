# Changelog

All notable changes to Gemma IA Offline will be documented in this file.

## [1.3] - 2025-07-17
### Added
- **Normal and Lite Versions**:
  - Multilingual support: English, Spanish, Russian via UI dropdown and `GemmaFiles/config.json`.
  - “Open GemmaFiles” button: Opens `GemmaFiles` folder from UI.
  - Startup progress bar: Tkinter-based for executable launch.
- **Lite Version**:
  - Added Tailwind CSS for a polished, responsive UI, matching Normal version.
- **Assets**: Added `icon-normal.ico` (flashlight) and `icon-lite.ico` (red dot) for executables.

### Changed
- Updated `src/lite/index_v1.3.html` to use Tailwind CSS.
- Removed color customization and knowledge base from Lite version for lower resource usage.
- Normal version: Retained `.pdf`/`.html` support with Tailwind CSS.
- Unified `README.md` for both versions.

### Fixed
- Improved error handling for low-memory scenarios and file operations.

## [1.2.6] - 2025-07-16
### Added
- **Lite Version (1.2.6)**:
  - Introduced lightweight version with `gemma2:2b` model (~1-2 GB VRAM).
  - Simplified chat interface with minimal CSS.
  - `.txt` file generation only.
- **Normal Version (1.2.6)**:
  - Improved file handling in `GemmaFiles`.

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