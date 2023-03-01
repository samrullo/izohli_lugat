# Introduction
This repo has scripts to OCR text written in uzbek cyrillic. Uzbek cyrillic contains additional character compared to russian cyrillic.

# PDF to images
Before OCR processing, we save PDF pages as images.
For that we use ```convert_from_path``` function from ```pdf2image``` library.

We will run this on ubuntu docker, because *pdf2image* works on Linux systems.

# OCR
To OCR uzbek text in cyrillic from an image we leverage ```pytesseract``` library
Below code assumes that *tesseract* and *uzb_cyrl* language pack is installed on the system

```python
txt = pytesseract.image_to_string(Image.open(img_folder/img_file), lang="uzb_cyrl")
```