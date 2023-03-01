import pathlib
from PIL import Image
import pytesseract
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')



folder=pathlib.Path(r"/var/datasets/izohli_lugat")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20 and d.name=="h_"]

for letter_directory in letter_directories:
    ocr_folder=letter_directory/"ocr_results"
    if not ocr_folder.exists():
        ocr_folder.mkdir(parents=True)
    img_folder=letter_directory/"images"
    if img_folder.exists():
        img_files=[f for f in img_folder.iterdir() if "jpg" in f.suffix]
        if len(img_files)>0:
            logging.debug(f"will process {len(img_files)} image files for letter directory {letter_directory}")
            ocr_results=[]
            for idx,img_file in enumerate(img_files):
                txt = pytesseract.image_to_string(Image.open(img_folder/img_file), lang="uzb_cyrl")
                txt_file=ocr_folder/(img_file.stem+".txt")
                txt_file.write_text(txt)
                ocr_results.append(txt)
                logging.debug(f"finished OCR on {idx}/{len(img_files)} {img_file.name}")
            
            # removed this as set does not preserve the order
            # ocr_results=list(set(ocr_results))
            # ocr_txt_file=ocr_folder/(letter_directory.name+"_whole_ocr.txt")
            # ocr_txt="\n".join(ocr_results)
            # ocr_txt=ocr_txt.replace("-\n","")
            # ocr_txt_file.write_text(ocr_txt)
            # logging.debug(f"saved {ocr_txt_file} with {len(ocr_results)} pages as one text")