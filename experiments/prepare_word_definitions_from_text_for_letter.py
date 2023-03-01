import pathlib
import nltk
import random
import re
from transformers import pipeline

nltk.download('punkt')

from nltk.tokenize import sent_tokenize

folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001\uzbek_tilining_izohli_lugati_t_www.ziyouz.com\ocr_result")
iz_file=folder/"iz_text.txt"

iz_text=iz_file.read_text(encoding="utf-8")
print(f"iz_text length : {len(iz_text)}")

from utils.izohli_lugat_utils import convert_cyrillic_to_latin

iz_text=convert_cyrillic_to_latin(iz_text)
print(f"iz_text length after converting to latin : {len(iz_text)}")

lines=iz_text.split("\n")
print(f"iz_text has {len(lines)} lines before removing garbage words")
# get rid of lines where www.ziyouz.com appears
garbage_words=["www.ziyouz.com"]
lines=[l for l in lines if all([gw not in l for gw in garbage_words])]
print(f"iz_text has {len(lines)} lines after removing garbage words")

letter_of_interest="T"

# first extracting any line that starts with the letter of interest
letter_lines=[(idx,l) for idx,l in enumerate(lines) if re.match(f"^{letter_of_interest}.*",l)]

# then further extracting lines where the first word is all uppercase, indicating this is the beginning of the definition
letter_lines=[(idx,l) for idx,l in letter_lines if l.split()[0].isupper()]

print(f"extracted {len(letter_lines)} letter lines")
word_definitions={}

for letter_start,letter_end in zip(letter_lines[:-1],letter_lines[1:]):
    start_idx,start_line=letter_start
    end_idx,end_line=letter_end
    word=start_line.split()[0]
    print(f"will prepare for word {word} starting at index {start_idx}")
    word_def="\n".join(lines[start_idx:end_idx])
    word_definitions[word]=word_def


wdeftup=tuple(word_definitions.items())

import json

def save_dict_to_json(d, filename):
    with open(filename, 'w') as f:
        json.dump(d, f)

file=folder/"t_letter_dict.json"
save_dict_to_json(word_definitions,file)