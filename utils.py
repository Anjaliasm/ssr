import os
import requests
import json

def download_pdf(pdf_url, folder):
    file_name = os.path.join(folder, os.path.basename(pdf_url))
    response = requests.get(pdf_url)

    with open(file_name, 'wb') as file:
        file.write(response.content)

    print(f'Downloaded: {file_name}')

def save_to_json(data, file_name):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

    print(f'Saved extracted data to: {file_name}')
