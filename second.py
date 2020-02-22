from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import requests

son_url = 'https://www.youtube.com/watch?v=cXP8OxMN_SQ'
son_html = urlopen(son_url).read().decode('utf-8')
son_soup = BeautifulSoup(son_html, 'lxml')

# get the title of the video and print it.
for title in son_soup.find_all('h1'):
    the_title = title.span
new_title = the_title.string

print(new_title.strip())

import os
if not os.path.exists(new_title.strip()):
    os.makedirs(new_title.strip())
print("Creat and Exam the Dir Successfully")

#get the url of the cover.
m = re.search('(?<=v=)...........', son_url)

#download the cover
cover_url = ('https://i.ytimg.com/vi/' + m.group(0) + '/maxresdefault.jpg')
r = requests.get(cover_url, stream=True)
image_name = (new_title.strip()+'.jpg')
with open((new_title.strip()+'/'+image_name), 'wb') as f:
    f.write(r.content)






# with open('test/%s' % image_name, 'wb') as f:
#     for chunk in r.iter_content(chunk_size=128):
#         f.write(chunk)
print('Saved %s' % image_name)
