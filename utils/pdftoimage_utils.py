import pathlib
from pdf2image import convert_from_path
import PyPDF2
import logging
from typing import Tuple,List

def get_pdf_page_number(pdf_file:pathlib):
    """
    returns number of pages in a pdf file
    """
    # Open the PDF file
    with open(pdf_file, 'rb') as fh:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(fh)
        # Get the number of pages
        num_pages = len(pdf_reader.pages)
        return num_pages
    


def generate_first_and_last_pages(pdf_page_numb: int, one_time_read_pages: int)->Tuple[List[int],List[int]]:
    """divides a PDF file into batches of a specified number of pages. 
      It returns two lists: first_pages and last_pages, which contain the starting
      and ending page numbers for each batch. This function is useful for 
      processing large PDF files.
    """
    if pdf_page_numb >= one_time_read_pages:
        first_pages = [
            i*one_time_read_pages for i in range(pdf_page_numb//one_time_read_pages)]
        last_pages = [
            (i+1)*one_time_read_pages for i in range(pdf_page_numb//one_time_read_pages)]
        remaining_pages = pdf_page_numb % one_time_read_pages
        first_pages.append(last_pages[-1])
        last_pages.append(last_pages[-1]+remaining_pages)
    else:
        first_pages = [0]
        last_pages = [pdf_page_numb]
    return first_pages, last_pages


def pdf_pages_to_images(folder: pathlib.Path, img_folder: pathlib.Path, pdf_filename: str, prefix_txt: str, one_time_read_pages=100, pause_every_iter=False):
    """
    converts a PDF file to images and saves them to a specified folder. 
    It can convert the PDF in batches and allows for 
    pausing between each batch. It's a useful tool for converting large PDF files.
    """
    pdf_page_numb = get_pdf_page_number(folder/pdf_filename)
    logging.debug(f"{pdf_filename} has {pdf_page_numb} pages")
    first_pages, last_pages = generate_first_and_last_pages(
        pdf_page_numb, one_time_read_pages)

    for read_round, (first_page, last_page) in enumerate(zip(first_pages, last_pages)):
        images = convert_from_path(
            folder/pdf_filename, first_page=first_page, last_page=last_page)
        logging.debug(
            f"converted {len(images)} pages, from {first_page} to {last_page}")

        for i, img in enumerate(images):
            img.save(img_folder/f"{prefix_txt}_{read_round}_{i}.jpg", "JPEG")

        if pause_every_iter:
            answer = input("coninue?")
            if answer.lower() in ["yes", "y"]:
                continue
            else:
                break
