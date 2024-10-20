import os
import requests
from bs4 import BeautifulSoup

from utils import download_pdf

BASE_URL = 'https://universalcollegeofengineering.edu.in/iqac/ssr-documents/'
PDF_FOLDER = 'ssr_pdfs'

def get_pdf_links():
    response = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the PDFs are linked in <a> tags
    links = soup.find_all('a', href=True)
    pdf_links = []

    for link in links:
        href = link['href']
        if href.endswith('.pdf'):
            pdf_links.append(href)

    return pdf_links

def main():
    if not os.path.exists(PDF_FOLDER):
        os.makedirs(PDF_FOLDER)

    pdf_links = get_pdf_links()

    for pdf_link in pdf_links:
        download_pdf(pdf_link, PDF_FOLDER)

if __name__ == '__main__':
    main()
