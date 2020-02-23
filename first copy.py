# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
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

for link in l3:
    print(link)
    print('\n')
print("Get All URL")
print("total =", len(l3))