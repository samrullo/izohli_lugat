from PIL import Image
import re
import pytesseract
import pathlib
import logging



def ocr_from_images(root_folder:pathlib.Path,lang="uzb_cyrl"):
    """
    OCR text from images in img_folder
    """
    ocr_folder=root_folder/"ocr_results"
    if not ocr_folder.exists():
        ocr_folder.mkdir(parents=True)
    img_folder=root_folder/"images"
    if img_folder.exists():
        img_files=[f for f in img_folder.iterdir() if "jpg" in f.suffix]
        if len(img_files)>0:
            logging.debug(f"will process {len(img_files)} image files for letter directory {root_folder}")
            ocr_results=[]
            for idx,img_file in enumerate(img_files):
                txt = pytesseract.image_to_string(Image.open(img_folder/img_file), lang="uzb_cyrl")
                txt_file=ocr_folder/(img_file.stem+".txt")
                txt_file.write_text(txt)
                ocr_results.append(txt)
                logging.debug(f"finished OCR on {idx}/{len(img_files)} {img_file.name}")

