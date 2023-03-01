import pathlib
import logging
import re
from collections import Counter
from typing import Dict,List

def detect_letter_from_long_text(long_text:str)->str:
    lines=long_text.split("\n")
    uppercase_words=[]
    for line in lines:
        words=re.findall("\w+",line)
        if len(words)>0:
            first_word=words[0]
            if first_word.isupper():
                uppercase_words.append(first_word)
    if len(uppercase_words)>0:
        first_letters=[w[0] for w in uppercase_words]
        first_letter_cnt=Counter(first_letters)
        most_frequent_letter,its_count=first_letter_cnt.most_common(1)[0]
        return most_frequent_letter

def get_word_definitions_for_letter(letter_of_interest:str,letter_whole_text:str,garbage_words:List=None,is_cyrillic=True)->Dict:
    """
    Get words and their definitions from lines list, assuming lines are related to dictionary of one letter
    """
    lines=letter_whole_text.split("\n")
    # get rid of lines where www.ziyouz.com appears
    if not garbage_words:
        garbage_words=["www.ziyouz.com"]
    lines=[l for l in lines if all([gw not in l for gw in garbage_words])]
    logging.debug(f"{letter_of_interest} whole text has {len(lines)} lines")
    # first extracting any line that starts with the letter of interest
    letter_lines=[(idx,l) for idx,l in enumerate(lines) if re.match(f"^{letter_of_interest}.*",l)]

    # then further extracting lines where the first word is all uppercase, indicating this is the beginning of the definition
    letter_lines=[(idx,l) for idx,l in letter_lines if l.split()[0].isupper()]

    logging.debug(f"extracted {len(letter_lines)} letter lines")
    word_definitions={}

    for letter_start,letter_end in zip(letter_lines[:-1],letter_lines[1:]):
        start_idx,start_line=letter_start
        end_idx,end_line=letter_end
        word=start_line.split()[0]
        logging.debug(f"will prepare for word {word} starting at index {start_idx}")
        word_def="\n".join(lines[start_idx:end_idx])
        word_definitions[word]=word_def
    if not is_cyrillic:
        word_definitions_latin={}
        for word,word_def in word_definitions.items():
            word_latin=convert_cyrillic_to_latin(word)
            word_def_latin=convert_cyrillic_to_latin(word_def)
            word_definitions_latin[word_latin]=word_def_latin
        return word_definitions_latin
    return word_definitions

def remove_word_at_start_of_long_text(word:str,long_text:str):
    tokens=long_text.split()
    if len(tokens)>0:
        if tokens[0].lower()==word:
            fixed_text=" ".join(tokens[1:])
        else:
            fixed_text=long_text
        return fixed_text


def extract_definitions(text):
    definitions = re.findall(r'\b\d+[.)]?\s+[^\d(]+', text)
    return definitions

def extract_number_from_string(txt:str):
    no_matches=re.findall("\d+",txt)
    return int(no_matches[0])

def extract_cluster_numb_and_page_numb_from_filename(filename:str,split_token:str="_"):
    tokens=filename.split(split_token)
    cluster_no_str, page_no_str=extract_number_from_string(tokens[-2]),extract_number_from_string(tokens[-1])
    return cluster_no_str,page_no_str

def read_all_txt_files_into_one_text(folder:pathlib.Path,concat_filename:str)->str:
    files=[f for f in folder.iterdir() if "txt" in f.suffix]
    logging.debug(f"will read {len(files)} into single text")
    concat_text=""
    for file in files:
        concat_text+=file.read_text(encoding="utf-8")
    concat_text=concat_text.replace("-\n","")
    concat_text_file=folder/concat_filename
    concat_text_file.write_text(concat_text)
    return concat_text

def get_uzb_cyrillic_to_laten_mapping_smallcase()->Dict:
    return {'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'j',
        'з': 'z',
        'и': 'i',
        'й': 'y',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'x',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'sh',
        'ъ': '‘',
        'ы': 'y',
        'ь': '‘',
        'э': 'e',
        'ю': 'yu',
        'я': 'ya',
        'ў':"o'",
        'қ':"q",
        'ғ':"g'",
        'ҳ':"h",}

def get_uzb_cyrillic_to_laten_mapping_uppercase()->Dict:
    return {        
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Yo',
        'Ж': 'J',
        'З': 'Z',
        'И': 'I',
        'Й': 'Y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'X',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Sh',
        'Ъ': '‘',
        'Ы': 'Y',
        'Ь': '‘',
        'Э': 'E',
        'Ю': 'Yu',
        'Я': 'Ya',
        'Ў':"O'",
        'Қ':"Q",
        'Ғ':"G'",
        "Ҳ":"H"

    }

def convert_cyrillic_to_latin(text:str)->str:
    cyrillic_to_latin = {**get_uzb_cyrillic_to_laten_mapping_smallcase(),**get_uzb_cyrillic_to_laten_mapping_uppercase()}
    latin_text = ""
    for char in text:
        if char in cyrillic_to_latin:
            latin_text += cyrillic_to_latin[char]
        else:
            latin_text += char
    return latin_text
