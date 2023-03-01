import os
import pathlib
from PIL import Image
import pytesseract

folder = pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat")
img_file="t_harfi_bir.jpg"
print(f"About to ocr file {folder/img_file}")

txt = pytesseract.image_to_string(Image.open(folder/img_file), lang="uzb_cyrl")
print(f"Find OCR processed result : \n {txt}")