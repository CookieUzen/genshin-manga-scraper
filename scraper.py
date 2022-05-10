#!/usr/bin/env python3

import wget
import zipfile
import requests
import os
import sys
from bs4 import BeautifulSoup

URL = sys.argv[1]
NAME = sys.argv[2]
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

images = soup.findAll("img", class_="viewer__img swiper-lazy")

url = []
for i in images:
    if i.get('src'):
        url.append(i['src'])
    else:
        url.append(i['data-src'])

with zipfile.ZipFile(NAME, 'w') as zip_f:
    for i in range(len(url)):
        print("Page " + str(i) + ": " + url[i])
        filename = str(i)+".jpg"
        wget.download(url[i], filename)
        zip_f.write(filename)
        print()
        os.remove(filename)
