import shutil
import requests

# Create a zip file
# Parameters: (output_name, format, directory_to_compress)
# This will create 'my_folder.zip' from the contents of 'path/to/folder'
shutil.make_archive('my_folder', 'zip', 'path/to/folder')

# Extract a zip file
# Parameters: (zip_file_to_extract, where_to_extract)
# This will extract 'my_folder.zip' into 'extract_here' directory
shutil.unpack_archive('my_folder.zip', 'extract_here')

# Download a file from the internet
# 1. Get the file from URL
# 2. Save it locally as 'downloaded_file.txt'
response = requests.get('https://example.com/file.txt')
with open('downloaded_file.txt', 'wb') as f:
    f.write(response.content)
