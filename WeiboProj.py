#!/usr/bin/env python
#coding=utf8

'''Author: Tuo LI
DATE: 04/july/2014'''
#from bs4 import BeautifulSoup

from LoginWeibo import *
from getWeiboPage import *


##import re
##import json
##import urllib2

##def parse_followings(page_content):# Parsing HTML
##    
##    #reguler expression to extract json data which contains html info
##    patt_view = '<script>FM.view\((.*)\)</script>'
##    patt = re.compile(patt_view, re.MULTILINE)
##    weibo_scripts = patt.findall(page_content)
##    for script in weibo_scripts:
##        view_json = json.loads(script)
##        if('html' in view_json and view_json['ns'] == 'pl.content.homeFeed.index'):
##            html = view_json['html']
##            soup = BeautifulSoup(html)	#WOW...we got the soup
##            
##    return soup


    #myurl = "http://www.weibo.com/p/1005051868663380/weibo?is_search=0&visible=0&is_ori=1&is_tag=0&profile_ftype=1&page=2#feedtop"
    #page1 = weiboLogin.Open(myurl)
    #soup = parse_followings(page1)
    #Text = soup.findAll('div', attrs={'class':'WB_text', 'node-type' : 'feed_list_content'})
 


if __name__ == '__main__':
    print "Start"
    weiboLogin = WeiboLogin('lituobuaa@hotmail.com', 'L_t2011!')#邮箱（账号）、密码
    if weiboLogin.Login() == True:
        print "登陆成功！"
        WBmsg = getWeiboPage()
        context = WBmsg.get_weibo(1005051868663380,1)

    

