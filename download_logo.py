import gdown
import os

# Create the directory if it doesn't exist
os.makedirs('autoreceipt/receiptgen/static/images', exist_ok=True)

# Google Drive file ID from the URL
file_id = '17WYeCknj_PPW8oYQiMOy-IwVOMvU6jcU'
output = 'autoreceipt/receiptgen/static/images/logo.png'

# Download the file
url = f'https://drive.google.com/uc?id={file_id}'
gdown.download(url, output, quiet=False) 