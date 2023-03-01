import pathlib
from PIL import Image

folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001\uzbek_tilining_izohli_lugati_t_www.ziyouz.com")
file="uzbek_tilining_izohli_lugati_t_www.ziyouz.com.pdf"
print(f"will process {file}, exists : {(folder/file).exists()}")

# below didn't work
with Image.open(folder/file) as pdf:
    n_frames=pdf.n_frames
    print(f"there are {len(n_frames)} frames")