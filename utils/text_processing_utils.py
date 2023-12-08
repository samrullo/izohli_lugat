import pathlib
from utils.izohli_lugat_utils import extract_cluster_numb_and_page_numb_from_filename
import logging
from collections import Counter
from typing import List
import re

def combine_ocr_results_into_one_text(ocr_folder:pathlib.Path):        
    txt_files=[file for file in ocr_folder.iterdir() if "whole_ocr" not in file.name]
    txt_file_keys=[extract_cluster_numb_and_page_numb_from_filename(file.name) for file in txt_files]
    
    # we are sorting txt_files in the correct order of clusters and page numbers
    txt_file_to_key={file:key for file,key in zip(txt_files,txt_file_keys)}
    txt_files=sorted(txt_files,key=lambda txt_file : txt_file_to_key[txt_file])
    
    # there can be cases where we have duplicate pages, we leverage Counter
    # to preserve the order of the pages and extract unique pages simultaneously
    texts=[txt_file.read_text(encoding="utf-8") for txt_file in txt_files]
    #breakpoint()
    texts=[remove_page_number_from_end(text,tail_line_no=5) for text in texts]
    texts=[remove_garbage_words(text,['www.ziyouz.com kutubxonasi', '\x0c'])for text in texts]
    texts=[combine_line_that_ends_with_hyphen_with_next_line(text) for text in texts]
    texts_counter=Counter(texts)
    unique_texts=[text for text,cnt in texts_counter.items()]
    
    filename=ocr_folder.parent.name+"_whole_ocr.txt"
    whole_ocr_txt_file=ocr_folder/filename
    whole_ocr_txt_file.write_text("\n".join(unique_texts),encoding="utf-8")
    logging.debug(f"finished saving {whole_ocr_txt_file}")

def combine_line_that_ends_with_hyphen_with_next_line(text:str):
    return text.replace("-\n","")

def remove_garbage_words(text:str,garbage_words:List[str]):
    for garbage_word in garbage_words:
        text=text.replace(garbage_word,"")
    return text

def remove_page_number_from_end(text:str,tail_line_no:int=5):
    lines=text.split("\n")
    head_lines=lines[:-1*tail_line_no]
    tail_lines=lines[-1*tail_line_no:]
    tail_lines=[l for l in tail_lines if not re.match("[0-9]+",l)]
    new_lines=head_lines+tail_lines
    return "\n".join(new_lines)
