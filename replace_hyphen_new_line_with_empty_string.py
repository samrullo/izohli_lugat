import json
import pathlib
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20]

all_word_defs={}
for letter_directory in letter_directories:
    word_defs_file=letter_directory/(letter_directory.name+"word_definitions_latin.json")
    # read json file into python dictionary
    with open(word_defs_file,"r") as fh:
        word_defs=json.load(fh)
    
    fixed_word_defs={}
    for word,word_def in word_defs.items():
        fixed_word_defs[word]=word_def.replace("-\n","")
    
    with open(word_defs_file,"w") as fh:
        json.dump(fixed_word_defs,fh)
    logging.debug(f"finished fixing {word_defs_file.name}")