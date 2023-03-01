from utils.izohli_lugat_utils import get_word_definitions_for_letter,detect_letter_from_long_text
import json
import pathlib
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20]

for letter_directory in letter_directories:
    ocr_result_folder=letter_directory/"ocr_results"
    letter_whole_text_file=ocr_result_folder/(letter_directory.name+"_whole_ocr.txt")
    logging.debug(f"Will extract word definitions from {letter_whole_text_file}")
    whole_text=letter_whole_text_file.read_text(encoding="utf-8")
    target_letter=detect_letter_from_long_text(whole_text)
    word_definitions=get_word_definitions_for_letter(target_letter,whole_text,is_cyrillic=False)
    
    # we want to convert words to small case letters
    word_small_case_definitions={}
    for word,word_def in word_definitions.items():
        word_small_case_definitions[word.lower()]=word_def
    word_defs_file=letter_directory/(letter_directory.name+"word_definitions_latin.json")
    with open(word_defs_file,"w") as fh:
        json.dump(word_small_case_definitions,fh)
    logging.debug(f"saved word definitions to {word_defs_file}")