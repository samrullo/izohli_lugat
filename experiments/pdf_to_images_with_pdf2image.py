import pathlib
from pdf2image import convert_from_path

folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001\uzbek_tilining_izohli_lugati_t_www.ziyouz.com")
file="uzbek_tilining_izohli_lugati_t_www.ziyouz.com.pdf"
print(f"will process {file}, exists : {(folder/file).exists()}")

images = convert_from_path(folder/file)
print(f"converted {len(images)} pages")