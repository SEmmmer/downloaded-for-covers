# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import requests
import sys

son_url = 'https://www.youtube.com/watch?v=nGURIAA0cT0'
son_html = urlopen(son_url).read().decode('utf-8')
son_soup = BeautifulSoup(son_html, 'lxml')

# get the url of the cover.
m = re.search('(?<=v=)[0-9a-zA-Z_]*', son_url)

# get the date of the video and print it.
date = son_soup.find('meta', {"itemprop":"startDate"})
if (str(date) == 'None') :
    date = son_soup.find('meta', {"itemprop":"datePublished"})
    date = date['content']
    date = (date + " 00:00:00")
else:
    date = date['content']
    date = date.replace('T', ' ')
    date = date.replace('+00:00', '')
print(date)

# get the title of the video and print it.
title = son_soup.find('span', {"id":"eow-title"})
title = title.get_text()
title = title.strip()
print(title)

# get info of the video
info = son_soup.find('p', {"id": "eow-description"})
print("Catch the info")

# download the cover.
cover_url = ('https://i.ytimg.com/vi/' + m.group(0) + '/maxresdefault.jpg')
r = requests.get(cover_url, stream=True)
image_name = (m.group(0) + '.jpg')
with open(('themes/hexo-theme-matery-develop/source/medias/covers/' + image_name), 'wb') as f:
    f.write(r.content)
print('Saved %s' % image_name)

# set the location of the cover.
img = '/medias/covers/' + m.group(0) + '.jpg'
coverImg = img

# creat the .md file.
with open ("source/_posts/" + m.group(0) + ".md", 'wb') as file:
    file.write("---" + "\n")
    file.write("title: " + "'" + title.encode('utf-8') + "'" + "\n")
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