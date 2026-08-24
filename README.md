# Comic-Translator

A Python project that translate the text of comics and images.

## Current Status

🚧 **In Development**

### Checkpoint 4
🚀 Phase 4 — OCR

Phase 4 has 3 milestones<br>
🎯 Phase 4.1 — Understand OCR<br>
🎯 Phase 4.2 — Python OCR<br>
🎯 Phase 4.3 — OCR Visualization<br>


🎯 Phase 4.2 goal


1. Install pytesseract by command:
```bash
uv add pytesseract 
```
2. Create new file with name 'ocr_test.py'.
3. Open comic images with Pillow.
4. Ask Tesseract for text
<br>  Use image_to_string() to extract text.
5. Use image_to_data() to get structured OCR data.
6. Access text, conf, left, top, width, and height.
7. Understand that OCR recognition, detection/location, and reading order are separate problems.
8. Extract the coordinates into Python and understand what they represent.