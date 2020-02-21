from __future__ import print_function

from bs4 import BeautifulSoup
from urllib2 import urlopen

# import requests

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

for link in l3:
    print(link)
    print('\n')
print("Get All URL")
print("total =", len(l3))

import os
if not os.path.exists('ytb'):
    os.makedirs('ytb')
print("Creat and Exam the Dir Successfully")



#     url = ul.find_all('img')
#     for img in imgs:
#         url = img['src']
#         r = requests.get(url, stream=True)
#         image_name = url.split('/')[-1]
#         with open('~/img/%s' % image_name, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=128):
#                 f.write(chunk)
#         print('Saved %s' % image_name)
