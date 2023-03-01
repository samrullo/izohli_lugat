import json
import pathlib
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")

letter_directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20]

all_word_defs={}
char_types={"cyr":"cyr","latin":"latin"}
char_type=char_types["latin"]
for letter_directory in letter_directories:
    word_defs_file=letter_directory/(letter_directory.name+f"word_definitions_{char_type}.json")
    # read json file into python dictionary
    with open(word_defs_file,"r") as fh:
        word_defs=json.load(fh)
    # combine all word_defs into one dictionary
    all_word_defs={**all_word_defs,**word_defs}
    logging.debug(f"finished processing {word_defs_file.name}")

all_word_defs_file=folder/f"izohli_lugat_word_definitions_{char_type}.json"
with open(all_word_defs_file,"w") as fh:
    json.dump(all_word_defs,fh)