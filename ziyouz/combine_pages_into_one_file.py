from utils.text_processing_utils import combine_ocr_results_into_one_text

import pathlib
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# folder=pathlib.Path(r"C:\Users\amrul\programming\nlp\uzbek_datasets\ziyouz\uzbek_nasri")
folder=pathlib.Path(r"/var/datasets/ziyouz/uzbek_nasri")

book_folders=[item for item in folder.iterdir() if item.is_dir()]
# book_folders=[folder/"oybek_mukammal_asarlar_to_plami_20_jildlik_12_jild_hikoyalar_ocherklar_start_400"]
force_copy=False
for i,book_folder in enumerate(book_folders):
    ocr_folder=book_folder/"ocr_results"
    filename=book_folder.name+"_whole_ocr.txt"
    whole_ocr_txt_file=ocr_folder/filename
    if whole_ocr_txt_file.exists() and not force_copy:
        logging.debug(f"{i+1}/{len(book_folders)} {whole_ocr_txt_file.name} exists so will skip")
        continue    
    logging.debug(f"{i+1}/{len(book_folders)} will combines pages of {book_folder.name} into one file")
    combine_ocr_results_into_one_text(ocr_folder)