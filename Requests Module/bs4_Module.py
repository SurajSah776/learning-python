# bs4 - BeautifulSoup
# used for web Scrapping
# pip install bs4

import requests
from bs4 import BeautifulSoup


# Website link to copy the code
r = requests.get("https://tiktokcoinrecharge.vercel.app/")
soup = BeautifulSoup(r.text, "html.parser")

html = soup.contents
html = soup.prettify()

with open("output1.html", "w") as file:
    file.write(str(html))

# print(r.text)
# print(soup.prettify())

# to print contents inside h2 tags only
for head in soup.find_all("h2"):
    print(head.text)
