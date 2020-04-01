# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import re

URL = "file:///Users/yangjinghua/Documents/shirakami/test.htm"
html = urlopen(URL)

soup = BeautifulSoup(html, 'lxml')
all_href = soup.find_all('a')

links = []
key_words = ['watch']

for s_l in all_href:
    if s_l.attrs.has_key('href'):
        links.append(s_l['href'])

l2 = {}.fromkeys(links).keys()
l3 = []

for i in l2:
    for j in key_words:
        if j in i:
            l3.append(i)
            break
error_video = ''
for son_url in l3:

    ifRequest = False
    while not ifRequest:
        try:
            son_html = urlopen(son_url).read().decode('utf-8')
            son_soup = BeautifulSoup(son_html, 'lxml')
            date = son_soup.find('meta', {"itemprop": "startDate"})
            if str(date) == 'None':
                date = son_soup.find('meta', {"itemprop": "datePublished"})
                date = date['content']
                date = (date + " 00:00:00")
            else:
                date = date['content']
                date = date.replace('T', ' ')
                date = date.replace('+00:00', '')
                print(date)
        except TypeError:
            ifRequest = False
            print("抓取网页失败，重新尝试抓取")
        else:
            ifRequest = True

    # check uploader
    uploader = son_soup.find('a', {"class": "yt-uix-sessionlink spf-link"})
    uploader = uploader['href']
    uploader = str(uploader)
    if uploader != '/channel/UCdn5BQ06XqgXoAxIhbqw5Rg':
        continue

    image = re.search('(?<=v=)...........', son_url)
    cover_url = ('https://i.ytimg.com/vi/' + image.group(0) + '/maxresdefault.jpg')
    image_name = (str(date) + '.jpg')

    ifRequest = False
    time = 0

    while not ifRequest:
        try:
            print("正在下载 " + image.group(0))
            f = urlopen(cover_url)
            data = f.read()
            with open('tmp/' + image_name, 'wb') as code:
                code.write(data)
        except:
            time += 1
            ifRequest = False
            print("获取封面失败，重新获取")
            if time >= 5:
                print("错误：该视频可能无封面，请在程序结束后检查")
                error_video += image.group(0)
                error_video += '\n'
                time = 0
                break
        else:
            ifRequest = True
            print("下载成功")

with open("errorList.txt", "wb") as error_video_list:
    error_video_list.write(error_video)

