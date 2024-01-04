# Command Line Utilities in python
# Image Downloader using Python by giving filename

import argparse
import requests


def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename


# Creating Parser
parser = argparse.ArgumentParser()

# Add command lines
parser.add_argument("url", help="Url of the file to download")
parser.add_argument("output", help="Name by which you want to save the file")

# Parse the arguments
args = parser.parse_args()

# Using the arguments in our code

print(args.url)
print(args.output)
download_file(args.url, args.output)
