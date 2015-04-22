#!/usr/bin/env python
#coding=utf8

'''Author: Houkai
DATE: 2013.12.23'''
from bs4 import BeautifulSoup

import re
import json
import urllib.request, urllib.error, urllib.parse
import http.cookiejar

import WeiboEncode
import WeiboSearch

class WeiboLogin:
    def __init__(self, user, pwd, enableProxy = False):
        "initilise WeiboLogin，enableProxy/ whether use Proxy or not, NOT by default"
        
        print("Initializing WeiboLogin...")
        self.userName = user
        self.passWord = pwd
        self.enableProxy = enableProxy
        print(("UserName: %s" %user))
        print(("Password: %s" %pwd))
        self.serverUrl = "http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.18)"
        self.loginUrl = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"
        self.postHeader = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'}

    def Login(self):
        "Login"
        self.EnableCookie(self.enableProxy)

        serverTime, nonce, pubkey, rsakv = self.GetServerTime()
        postData = WeiboEncode.PostEncode(self.userName, self.passWord, serverTime, nonce, pubkey, rsakv)#加密用户和密码
        print(("Post data length: %s \n" %len(postData)))
        print(postData)

        req = urllib.request.Request(self.loginUrl, postData, self.postHeader)
        print("Posting request...")
        result = urllib.request.urlopen(req)
        text = result.read()
        try:
            loginUrl = WeiboSearch.sRedirectData(text)
            print(loginUrl)
            if 'retcode=0' in loginUrl:
                print("Re-direct url success!!")
                x =urllib.request.urlopen(loginUrl)
                print(x.read())
                print('Login sucess!')
                return True
            else:
                print('Login Failed!')
                return False
        except:
            print('Login error!')
            return False

            
        


    def GetServerTime(self):
        
        "Get server time and nonce, which are used to encode the password"

        print("Getting server time and nonce...")
        serverData = urllib.request.urlopen(self.serverUrl).read()#得到网页内容
        print(serverData)

        try:
            serverTime, nonce, pubkey, rsakv = WeiboSearch.sServerData(serverData)#解析得到serverTime，nonce等
            return serverTime, nonce, pubkey, rsakv
        except:
            print('Get server time & nonce error!')
            return None


    def EnableCookie(self, enableProxy):
        "Enable cookie & proxy (if needed)."

        cookiejar = http.cookiejar.LWPCookieJar()#建立cookie
        cookie_support = urllib.request.HTTPCookieProcessor(cookiejar)

        if enableProxy:
            proxy_support = urllib.request.ProxyHandler({'http':'http://xxxxx.pac'})#使用代理
            opener = urllib.request.build_opener(proxy_support, cookie_support, urllib.request.HTTPHandler)
            print("Proxy enabled")
        else:
            opener = urllib.request.build_opener(cookie_support, urllib.request.HTTPHandler)

        urllib.request.install_opener(opener)#构建cookie对应的opener

    def Open(self,anyurl):
        x = urllib.request.urlopen(anyurl)
        return x.read()
        



