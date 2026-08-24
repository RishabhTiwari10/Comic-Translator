# Comic-Translator

A Python project that translate the text of comics and images.

## Current Status

🚧 **In Development**

### Checkpoint 4
🚀 Phase 4 — OCR

Phase 4 has 3 milestones
🎯 Phase 4.1 — Understand OCR
🎯 Phase 4.2 — Python OCR
🎯 Phase 4.3 — OCR Visualization


🎯 Phase 4.1 goal


Confirm:
Tesseract installed       ✅
Tesseract executable      ✅
Tesseract can read image  ✅

And run:
tesseract input/image_1.jpeg output_psm3 --psm 3
tesseract input/image_1.jpeg output_psm6 --psm 6
tesseract input/image_1.jpeg output_psm11 --psm 11
tesseract input/image_1.jpeg output_data --psm 11 tsv

Then answer following question:
1. Which PSM gave the best result?
2. Did any of them detect dialogue that the others missed?
3. Is the text still out of order?
4. Does output_data.tsv contain the left, top, width, height, conf, and text information?