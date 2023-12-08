from utils.ocr_utils import ocr_from_images

import pathlib
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

folder=pathlib.Path(r"/var/datasets/ziyouz/uzbek_nasri")

book_folders=[item for item in folder.iterdir() if item.is_dir()]

for book_idx,book_folder in enumerate(book_folders):
    images_folder=book_folder/"images"
    ocr_results_folder=book_folder/"ocr_results"
    should_ocr=True
    if images_folder.exists():        
        img_files=[file for file in images_folder.iterdir() if "jpg" in file.suffix]        
        if ocr_results_folder.exists():
            ocr_files=[file for file in ocr_results_folder.iterdir() if "txt" in file.suffix and "whole_ocr" not in file.name]
            if len(ocr_files)==len(img_files):
                should_ocr=False            
        if should_ocr:
            logging.debug(f"** {book_idx+1}/{len(book_folders)} Will OCR {book_folder} **")
            ocr_from_images(book_folder,lang="uzb_cyrl")
            logging.debug(f"** {book_idx+1}/{len(book_folders)} Finished OCRing {book_folder} **")
        else:
            logging.debug(f"** {book_idx+1}/{len(book_folders)} Will skip OCR {book_folder} since it already finished**")