# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import json
import sys

print(sys.stdout.encoding)


text = ''
with open("1.html",'rb') as f:
    text = f.read()

patt_view = b'<script>FM.view\((.*)\)</script>'
patt = re.compile(patt_view,re.MULTILINE) 

rightpart = patt.findall(text)
view_json = json.loads(rightpart[27].decode('utf-8'))
if('html' in view_json and view_json['ns'] == 'pl.content.homeFeed.index'):
    print("Got it!!")
    soup = BeautifulSoup(view_json['html'])

#x = soup.find("div","WB_text W_f14")
x = soup.find("div",attrs={'class':'WB_text', 'node-type' : 'feed_list_content'})

with open("x.txt",'w') as f:
    f.write(soup.prettify())
