# Import the packages os and urllib.request
import os
import urllib.request

# Create a directory in our project folder if it doesn't exist
os.makedirs('titanic-data', exist_ok=True)

# Set the source URL and destination path
download_url = 'https://hbiostat.org/data/repo/titanic3.csv'
file_path = 'titanic-data/titanic3.csv'

# Download the file if it doesn't exist
if not os.path.exists(file_path):
   urllib.request.urlretrieve(download_url, file_path)