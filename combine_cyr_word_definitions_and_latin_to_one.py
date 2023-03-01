import json
import pathlib
import logging
from utils.izohli_lugat_utils import convert_cyrillic_to_latin

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

wd_cyr_file=folder/"izohli_lugat_word_definitions_cyr.json"

with open(wd_cyr_file,"r") as fh:
    wd_cyr=json.load(fh)

logging.debug(f"loaded {len(wd_cyr)} cyr word definitions")

#to store word definition records
wd=[]
wd_cyr_to_latin={}

for word,word_def in wd_cyr.items():    
    word_latin=convert_cyrillic_to_latin(word)
    word_def_latin=convert_cyrillic_to_latin(word_def)
    word_record={"cyr":word,"cyr_def":word_def,"latin":word_latin,"latin_def":word_def_latin}    
    wd_cyr_to_latin[word]=word_latin
    wd.append(word_record)

with open(folder/"izohli_lugat_word_records.json","w") as fh:
    json.dump(wd,fh)
logging.debug(f"saved {len(wd)} word records")