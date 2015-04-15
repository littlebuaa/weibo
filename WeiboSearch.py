#!/usr/bin/env python
#coding=utf8

'''Author: Houkai
DATE: 2013.12.23'''

import re
import json

def sServerData(serverData):
    "Search the server time & nonce from server data"
    print("----------Search the server time & nonce-------------")
    p = re.compile(b'\((.*)\)')
    jsonData = p.search(serverData).group(1)
    data = json.loads(jsonData.decode())
    serverTime = str(data['servertime'])
    nonce = data['nonce']
    pubkey = data['pubkey']#
    rsakv = data['rsakv']# 
    print(("Server time is: %s" %serverTime))
    print(("Nonce is: %s"%nonce))
    return serverTime, nonce, pubkey, rsakv


def sRedirectData(text):
    p = re.compile(b'location\.replace\([\'"](.*?)[\'"]\)')
    loginUrl = p.search(text).group(1)
    return loginUrl.decode()
