import pathlib
import nltk

nltk.download('punkt')

from nltk.tokenize import sent_tokenize

folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001\uzbek_tilining_izohli_lugati_t_www.ziyouz.com\ocr_result")
files=[f for f in folder.iterdir() if "txt" in f.suffix]
print(f"will read {len(files)} into single text")

iz_text=""

for file in files:
    iz_text+=file.read_text(encoding="utf-8")

iz_text=iz_text.replace("-\n","")
sentences=sent_tokenize(iz_text)
print(f"extracted total of {len(sentences)} sentences")



iz_text_file=folder/"iz_text.txt"
iz_text_file.write_text(iz_text)