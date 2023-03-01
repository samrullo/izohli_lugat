import pathlib
import zipfile

garbage_words=["uzbek_tilining_izohli_lugati_","www.ziyouz.com"]

folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\izohli_lugat\drive-download-20230121T035915Z-001")
zipfiles=[f for f in folder.iterdir() if "zip" in f.suffix]

for zfile in zipfiles:
    with zipfile.ZipFile(zfile,"r") as zref:
        new_fname=zfile.stem
        for gbw in garbage_words:
            new_fname=new_fname.replace(gbw,"")
        zref.extractall(folder/new_fname)
    print(f"finished decompressing {new_fname}")