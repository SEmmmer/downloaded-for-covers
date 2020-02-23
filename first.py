# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import os
import re
import requests
import sys

html = urlopen("file:///Users/yangjinghua/Documents/a%20Python%20program/shirakamifubuki.htm")
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

for son_url in l3:
    print(son_url)
    son_html = urlopen(son_url).read().decode('utf-8')
    son_soup = BeautifulSoup(son_html, 'lxml')

    # get the date of the video and print it.
    fake_random = 1
    date = son_soup.find('meta', {"itemprop":"startDate"})
    if (str(date) == 'None') :
        date = son_soup.find('meta', {"itemprop":"datePublished"})
        date = date['content']
        date = (date + " 00:00:0" + str(fake_random))
        fake_random += 1
        if(fake_random == 9):
            fake_random = 1
    else:
        date = date['content']
        date = date.replace('T', ' ')
        date = date.replace('+00:00', '')
    date2 = date.replace(':', '_').replace(' ', '_')
    print(date)

    # does the file already exist?
    if(os.path.exists("source/_posts/" + date2 + ".md")):
        print("file already exist!!!!!!!!!!")
        continue

    # get the title of the video and print it.
    title = son_soup.find('span', {"id":"eow-title"})
    title = title.get_text()
    title = title.strip()
    print(title)

    # get info of the video
    info = son_soup.find('p', {"id": "eow-description"})
    print("Catch the info")

    # get the url of the cover.
    m = re.search('(?<=v=)[0-9a-zA-Z_]*', son_url)

    # download the cover.
    cover_url = ('https://i.ytimg.com/vi/' + m.group(0) + '/maxresdefault.jpg')
    r = requests.get(cover_url, stream=True)
    image_name = (date2 + '.jpg')
    with open(('themes/hexo-theme-matery-develop/source/medias/covers/' + image_name), 'wb') as f:
        f.write(r.content)
    print('Saved %s' % image_name)

    # set the location of the cover.
    img = '/medias/covers/' + date2 + '.jpg'
    coverImg = img

    # creat the .md file.
    with open ("source/_posts/" + date2 + ".md", 'wb') as file:
        file.write("---" + "\n")
        file.write("title: " + title.encode('utf-8') + "\n")
        file.write("date: " + date + "\n")
        file.write("img: " + img + "\n")
        file.write("cover: true" + "\n")
        file.write("coverImg: " + img + "\n")
        file.write("tags:" + "\n")
        file.write("  - Youtube Streaming" + "\n")
        file.write("---" + "\n")
        file.write("\n")
        file.write(str(son_url))
        file.write("\n")
        file.write(str(info))
        file.close()
    print("Creat the .md file")
    # TODO:local exam
print("finished")