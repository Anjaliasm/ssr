import pdfplumber
import os
from utils import save_to_json

def extract_pdf_data(pdf_path):
    extracted_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            page_data = {
                'page_number': page_number,
                'text': page.extract_text(),
                'links': []
            }

            # Safely handle annotations (if they exist)
            if hasattr(page, 'annotations') and page.annotations:
                for annotation in page.annotations:
                    if annotation.get('uri'):
                        page_data['links'].append(annotation['uri'])

            extracted_data.append(page_data)
    return extracted_data

def main():
    # Folder where the PDFs are stored
    pdf_folder = 'ssr_pdfs'  # Make sure this is the folder where PDFs are stored
    output_file = 'extracted_data.json'

    # Get all PDF files in the folder
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]

    extracted_data = []
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        print(f"Extracting data from {pdf_file}...")
        extracted_data.extend(extract_pdf_data(pdf_path))

    # Save the extracted data to a JSON file
    save_to_json(extracted_data, output_file)
    print(f"Data extraction complete! Saved to {output_file}")

if __name__ == "__main__":
    main()
