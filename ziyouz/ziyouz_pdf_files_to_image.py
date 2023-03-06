import shutil
from utils.pdftoimage_utils import pdf_pages_to_images
import pathlib
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

folder=pathlib.Path(r"/var/datasets/ziyouz/uzbek_nasri")

pdf_files=[file for file in folder.iterdir() if "pdf" in file.suffix]
logging.debug(f"will convert pdf to images for {len(pdf_files)} pdf files")

pause_on_iters=100

for pdf_idx,pdf_file in enumerate(pdf_files):
    pdf_folder=folder/pdf_file.stem
    if not pdf_folder.exists():
        pdf_folder.mkdir(parents=True)
    #let's move origin pdf file to its own folder
    shutil.move(pdf_file,pdf_folder/pdf_file.name)    
    images_folder=pdf_folder/"images"
    if not images_folder.exists():
        images_folder.mkdir(parents=True)
    pdf_pages_to_images(pdf_folder,images_folder,pdf_file.name,pdf_file.stem,one_time_read_pages=100,pause_every_iter=False)
    logging.debug(f"*** {pdf_idx}/{len(pdf_files)} FINISHED EXTRACTING IMAGES FROM {pdf_file.name} ***")