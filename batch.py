#!/usr/bin/env python3

import os

list = ["https://ys.mihoyo.com/main/manga/detail/191?mute=1",
"https://ys.mihoyo.com/main/manga/detail/192?mute=1",
"https://ys.mihoyo.com/main/manga/detail/198?mute=1",
"https://ys.mihoyo.com/main/manga/detail/429?mute=1",
"https://ys.mihoyo.com/main/manga/detail/438?mute=1",
"https://ys.mihoyo.com/main/manga/detail/443?mute=1",
"https://ys.mihoyo.com/main/manga/detail/482?mute=1",
"https://ys.mihoyo.com/main/manga/detail/810?mute=1",
"https://ys.mihoyo.com/main/manga/detail/917?mute=1",
"https://ys.mihoyo.com/main/manga/detail/987?mute=1",
"https://ys.mihoyo.com/main/manga/detail/1073?mute=1",
"https://ys.mihoyo.com/main/manga/detail/3476?mute=1",
"https://ys.mihoyo.com/main/manga/detail/3756?mute=1",
"https://ys.mihoyo.com/main/manga/detail/6144?mute=1",
"https://ys.mihoyo.com/main/manga/detail/6477?mute=1",
"https://ys.mihoyo.com/main/manga/detail/6530?mute=1"]

print(list)

for i in range(len(list)):
    print(i)
    os.system("./scraper.py " + list[i] + " \'Chapter " + str(i+1) + ".cbz\'")
