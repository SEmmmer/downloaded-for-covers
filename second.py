from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import requests

son_html = urlopen('https://www.youtube.com/watch?v=cXP8OxMN_SQ').read().decode('utf-8')
son_soup = BeautifulSoup(son_html, 'lxml')

# get the title of the video and print it.
for title in son_soup.find_all('h1'):
    new_title = title.span
print(new_title.string)

#get the url to get img.
m = re.search('(?<=v=)...........', 'https://www.youtube.com/watch?v=cXP8OxMN_SQ')

#download the cover
cover_url = ('https://i.ytimg.com/vi/' + m.group(0) + '/maxresdefault.jpg')
print(cover_url)
r = requests.get(cover_url, stream=True)
image_name = cover_url.split('/')[-1]
with open('test/%s' % image_name, 'wb') as f:
    for chunk in r.iter_content(chunk_size=128):
        f.write(chunk)
print('Saved %s' % image_name)
