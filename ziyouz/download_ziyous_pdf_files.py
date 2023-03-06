from bs4 import BeautifulSoup
import requests
import urllib.request
import pathlib
import re
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


url = 'https://n.ziyouz.com/kutubxona/category/41-o-zbek-nasri?start=0'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

domain_name="https://n.ziyouz.com/"

def get_pdf_links(soup:BeautifulSoup,pdf_indicator:str="download",domain_name=domain_name):
    pdf_links = [domain_name+link.get('href') for link in soup.find_all('a') if link.get('href') and pdf_indicator in link.get('href')]
    return list(set(pdf_links))

def get_filename_from_link(link:str):
    filename="not_set_yet"
    link_chunks=re.split(r'\d+.*\d+:',link)
    if len(link_chunks)>0:
        filename=link_chunks[-1]
        filename="_".join(re.findall("\w+",filename))    
    return filename+".pdf"

def get_page_links(soup:BeautifulSoup,page_url_header:str="/kutubxona/category/41-o-zbek-nasri?start",domain_name:str=domain_name):    
    links=soup.find_all('a')
    page_links=[link.get('href') for link in links if link.get('href') and page_url_header in link.get('href')]
    page_links=[domain_name+link for link in page_links]
    return page_links


force_copy=False
folder=pathlib.Path(r"C:\Users\amrul\programming\datasets\uzbek_nlp_dataset\ziyouz\uzbek_nasri")

page_links=get_page_links(soup)
logging.debug(f"retrieved {len(page_links)} page links")
for page_link in page_links:
    response = requests.get(page_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links=get_pdf_links(soup)
    for i,link in enumerate(pdf_links):
        filename=get_filename_from_link(link)
        filepath=folder/filename
        if not filepath.exists() or force_copy:
            resp=requests.get(link)
            with open(folder/filename,"wb") as fh:
                fh.write(resp.content)
            logging.debug(f"*** {i}/{len(pdf_links)} FINISHED DOWNLOADING {filename} ***")
        else:
            logging.debug(f"*** {i}/{len(pdf_links)} {filepath} ALREADY EXISTS ***")
