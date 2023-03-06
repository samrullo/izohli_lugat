from PIL import Image
import pytesseract
import pathlib
import logging


def ocr_from_images(img_folder:pathlib.Path,ocr_folder:pathlib.Path,lang="uzb_cyrl"):
    """
    OCR text from images in img_folder
    """
    txt_list=[]
    if img_folder.exists():
        img_files=[f for f in img_folder.iterdir() if "jpg" in f.suffix]        
        if len(img_files)>0:
            logging.debug(f"will process {len(img_files)} image files in {img_folder}")
            ocr_results=[]
            for idx,img_file in enumerate(img_files):
                txt = pytesseract.image_to_string(Image.open(img_folder/img_file), lang=lang)
                txt_file=ocr_folder/(img_file.stem+".txt")
                txt_file.write_text(txt)
                ocr_results.append(txt)
                logging.debug(f"finished OCR on {idx}/{len(img_files)} {img_file.name}")
                txt_list.append(txt)
        return txt_list
    else:
        logging.debug(f"{img_folder} doesn't exist")
        return txt_list
