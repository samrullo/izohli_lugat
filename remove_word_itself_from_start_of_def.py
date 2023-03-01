from utils.izohli_lugat_utils import get_word_definitions_for_letter,detect_letter_from_long_text
import json
import pathlib
import re
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20]

for letter_directory in letter_directories:
    word_defs_file=letter_directory/(letter_directory.name+"word_definitions_latin.json")
    with open(word_defs_file,"r") as fh:
        word_defs=json.load(fh)
    fixed_word_defs={}
    for word,word_def in word_defs.items():
        tokens=word_def.split(word.upper())
        
        # remove non alphabet characters from the word
        if re.match(".*\W+.*",word):
            word="".join([wc for wc in word if not re.match("\W+",wc)])
        
        # remove the word itself from the word definition
        if len(tokens)>0:
            # assume that we could match word at the start of the meaning
            fixed_word_defs[word]="".join(tokens[1:])
        else:
            fixed_word_defs[word]=word_def
    
    with open(word_defs_file,"w") as fh:
        json.dump(fixed_word_defs,fh)
    logging.debug(f"finished fixing {word_defs_file.name}")
