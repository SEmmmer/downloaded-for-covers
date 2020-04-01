# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import re

if not os.path.exists('./video.htm'):
    print('请将 htm 格式的网页命名为 video.htm 后放在这个文件夹')
    print('建议使用谷歌浏览器下载网页')
    exit(1)

URL = "file:./video.htm"
html = urlopen(URL)

if not os.path.exists('./buffer'):
    os.makedirs('./buffer')
if not os.path.exists('./tmp'):
    os.makedirs('./tmp')

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

time = 0

for son_url in l3:
    image = re.search('(?<=v=)...........', son_url)

    # 此处为封面存在检测，如果需要将封面全部更新，请注释掉以下三行代码 #
    if os.path.exists('buffer/' + image.group(0) + '.jpg'):
        print('文件已存在，该封面将被跳过')
        continue
    ###########################################################

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
            time += 1
            ifRequest = False
            print("抓取网页失败，重新尝试抓取")
            if time >= 5:
                print("错误：该链接可能不存在，请在程序结束后检查")
                with open("errorList.txt", "ab") as code:
                    code.write('https://www.youtube.com/watch?v=' + image.group(0) + ' 网页不存在\n')
                time = 0
                break
        else:
            ifRequest = True

    # check uploader
    # can change to other uploader
    uploader = son_soup.find('a', {"class": "yt-uix-sessionlink spf-link"})
    uploader = str(uploader['href'])
    if uploader != '/channel/UCdn5BQ06XqgXoAxIhbqw5Rg':
        continue

    cover_url = ('https://i.ytimg.com/vi/' + image.group(0) + '/maxresdefault.jpg')
    image_name = (str(date) + '.jpg')
    buffer_image_name = (image.group(0) + '.jpg')

    ifRequest = False
    while not ifRequest:
        try:
            print("正在下载 " + image.group(0))
            f = urlopen(cover_url)
            data = f.read()
            with open('tmp/' + image_name, 'wb') as code:
                code.write(data)
            with open('buffer/' + buffer_image_name, 'wb') as code:
                code.write(data)
        except:
            time += 1
            ifRequest = False
            print("获取封面失败，重新获取")
            if time >= 5:
                print("错误：该视频可能无封面，请在程序结束后检查")
                with open("errorList.txt", "ab") as code:
                    code.write('https://www.youtube.com/watch?v=' + image.group(0) + ' 封面不存在\n')
                time = 0
                break
        else:
            ifRequest = True
            print("下载成功")
print('程序结束')
