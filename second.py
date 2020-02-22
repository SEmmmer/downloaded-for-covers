from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import requests

son_url = 'https://www.youtube.com/watch?v=kDhtLZh7a7U&t=1719s'
son_html = urlopen(son_url).read().decode('utf-8')
son_soup = BeautifulSoup(son_html, 'lxml')

# get the date of the video
date = son_soup.find('meta', {"itemprop":"datePublished"})
print(date['content'])

# get the title of the video and print it.
title = son_soup.find('span', {"class":"title"})
new_title = title.get_text()
print(new_title.strip())

import os
if not os.path.exists(new_title.strip()):
    os.makedirs(new_title.strip())
print("Creat and Exam the Dir Successfully")

#get the url of the cover.
m = re.search('(?<=v=)[0-9a-zA-Z_]*', son_url)

#download the cover
cover_url = ('https://i.ytimg.com/vi/' + m.group(0) + '/maxresdefault.jpg')
r = requests.get(cover_url, stream=True)
image_name = (new_title.strip()+'.jpg')
with open((new_title.strip()+'/'+image_name), 'wb') as f:
    f.write(r.content)
print('Saved %s' % image_name)
