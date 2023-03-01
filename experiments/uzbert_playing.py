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
gaplar=sent_tokenize(iz_text)
print(f"extracted total of {len(gaplar)} sentences")


unmasker = pipeline('fill-mask', model='coppercitylabs/uzbert-base-uncased')

picked_gap=random.choice(gaplar)
print(f"picked up gap : {picked_gap}")
words=re.findall("\w+",picked_gap)
picked_word=random.choice(words)
print(f"picked word for masking: {picked_word}")
masked_gap=picked_gap.replace(picked_word,"[MASK]")
unmasked_result=unmasker(masked_gap)
print(f"unmask result : {unmasked_result}")