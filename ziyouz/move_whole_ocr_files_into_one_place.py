from utils.text_processing_utils import combine_ocr_results_into_one_text
import shutil

import pathlib
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# folder=pathlib.Path(r"C:\Users\amrul\programming\nlp\uzbek_datasets\ziyouz\uzbek_nasri")
folder=pathlib.Path(r"/var/datasets/ziyouz/uzbek_nasri")
target_folder=folder/"whole_ocr_collection"
if not target_folder.exists():
    target_folder.mkdir(parents=True)

book_folders=[item for item in folder.iterdir() if item.is_dir()]


for i,book_folder in enumerate(book_folders):
    ocr_folder=book_folder/"ocr_results"
    filename=book_folder.name+"_whole_ocr.txt"
    whole_ocr_txt_file=ocr_folder/filename
    if whole_ocr_txt_file.exists():
        logging.debug(f"{i+1}/{len(book_folders)} will copy {whole_ocr_txt_file.name} to target folder")
        shutil.copy(whole_ocr_txt_file,target_folder/whole_ocr_txt_file.name)
    else:
        logging.debug(f"{i+1}/{len(book_folders)}  {whole_ocr_txt_file.name} file doesn't exist")
