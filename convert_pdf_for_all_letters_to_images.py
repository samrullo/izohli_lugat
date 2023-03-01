import pathlib
from utils.pdftoimage_utils import pdf_pages_to_images
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def get_single_pdf_file_in_directory(folder:pathlib.Path)->pathlib.Path:
    pdf_files=[f for f in folder.iterdir() if "pdf" in f.suffix]
    if len(pdf_files)>0:
        return pdf_files[0]

folder=pathlib.Path(r"/var/datasets/izohli_lugat")

directories=[d for d in folder.iterdir() if d.is_dir() and len(d.name)<20 and d.name=="h_"]
force_generate=True
for directory in directories:
    pdf_file=get_single_pdf_file_in_directory(directory)
    logging.info(f"will process pdf file : {pdf_file}")
    img_folder=directory/"images"
    if not img_folder.exists():
        img_folder.mkdir(parents=True)    
    files_in_img_folder=list(img_folder.iterdir())
    if len(files_in_img_folder)==0 or force_generate:
        prefix_text=directory.name.replace("-","")
        pdf_pages_to_images(directory,img_folder,pdf_file.name,prefix_text,one_time_read_pages=50)