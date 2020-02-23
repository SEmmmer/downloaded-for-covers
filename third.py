# -*- coding: utf-8 -*
from __future__ import print_function
from bs4 import BeautifulSoup
from urllib2 import urlopen
import re
import requests
import sys



title = '【#ホロ人狼】狐を探せ！ホロライブ★ワードフォックス【ワード人狼】'
date = '2019-02-26 14:00:18'
# 2019-02-26 14:00:18
date2 = date.replace(':', '_').replace(' ', '_')
# 2019-02-26_14_00_18
img = '/medias/covers/' + date2 + '.jpg'
coverImg = img
with open ("source/_posts/" + date2 + ".md", 'wb') as file:
    file.write("---" + "\n")
    file.write("title: " + title + "\n")
    file.write("date: " + date + "\n")
    file.write("img: " + img + "\n")
    file.write("cover: true" + "\n")
    file.write("coverImg: " + img + "\n")
    file.write("tags:" + "\n")
    file.write("  - Youtube Streaming" + "\n")
    file.write("---" + "\n")
    file.close()
# ---
# title: typora-vue-theme主题介绍
# date: 2018-09-07 09:25:00
# img: /source/images/xxx.jpg
# cover: true
# coverImg: /images/1.jpg
# tags:
#   - Youtube Streaming
# ---