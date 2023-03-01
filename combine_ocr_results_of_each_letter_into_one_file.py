import pathlib
from collections import Counter
from utils.izohli_lugat_utils import extract_cluster_numb_and_page_numb_from_filename
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')



folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20]

for letter_directory in letter_directories:
    ocr_folder=letter_directory/"ocr_results"
    txt_files=[file for file in ocr_folder.iterdir() if "whole_ocr" not in file.name]
    txt_file_keys=[extract_cluster_numb_and_page_numb_from_filename(file.name) for file in txt_files]
    
    # we are sorting txt_files in the correct order of clusters and page numbers
    txt_file_to_key={file:key for file,key in zip(txt_files,txt_file_keys)}
    txt_files=sorted(txt_files,key=lambda txt_file : txt_file_to_key[txt_file])
    
    # there can be cases where we have duplicate pages, we leverage Counter
    # to preserve the order of the pages and extract unique pages simultaneously
    texts=[txt_file.read_text(encoding="utf-8") for txt_file in txt_files]
    texts_counter=Counter(texts)
    unique_texts=[text for text,cnt in texts_counter.items()]
    
    whole_ocr_txt_file=ocr_folder/(letter_directory.name+"_whole_ocr.txt")
    whole_ocr_txt_file.write_text("\n".join(unique_texts),encoding="utf-8")
    logging.debug(f"finished saving {whole_ocr_txt_file}")
