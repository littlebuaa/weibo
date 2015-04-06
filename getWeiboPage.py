#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import urllib2
##import sys
#import time

from bs4 import BeautifulSoup
import re
import json

##reload(sys)
##sys.setdefaultencoding('utf-8')

def parse_followings(page_content):
    
    #reguler expression to extract json data which contains html info
    patt_view = '<script>FM.view\((.*)\)</script>'
    patt = re.compile(patt_view, re.MULTILINE)
    weibo_scripts = patt.findall(page_content)
    for script in weibo_scripts:
        view_json = json.loads(script)
        if('html' in view_json and view_json['ns'] == 'pl.content.homeFeed.index'):
            html = view_json['html']
            soup = BeautifulSoup(html)	#WOW...we got the soup
            
    return soup


class getWeiboPage:

    body1 = {
        'pids':'Pl_Official_LeftProfileFeed__26',
        'is_search':'0',
        'visible':'0',
        'is_ori':'1',
        'is_tag':'0',
        'profile_ftype':'1',
        'page':'8',
        '__ref' : '/p/1005051868663380/weibo',
        '_t':'FM_140466115578417'
    }
    
    body = {
            '_wv':'5',
            'domain':'100505',
            'pre_page':'8',
            'page':'8',
            'count':'15',
            'pagebar':'1',
            'max_msign':'',	
            'filtered_min_id':'',	
            'pl_name':'Pl_Official_LeftProfileFeed__26',
            'id':'1005051868663380',
            'script_uri':'/p/1005051868663380/weibo',
            'feed_type':'0'
    }
    uid_list = []
    #uid = 1005051868663380
    charset = 'utf8'

    def get_weibo(self,uid,page):
            getWeiboPage.body['id'] = uid
            getWeiboPage.body['page'] = page
            getWeiboPage.body1['page'] = page
            url = self.get_url(uid)
            x =self.get_firstpage(url)
            y =self.get_secondpage(url)
            z =self.get_thirdpage(url)
            return (x,y,z)
    def get_firstpage(self,url):
            getWeiboPage.body['pre_page'] = getWeiboPage.body['page']
            url = url +'?'+ urllib.urlencode(getWeiboPage.body1)
            req = urllib2.Request(url)
            result = urllib2.urlopen(req)
            page = result.read()
            soup = parse_followings(page)
            text = soup.findAll('div', attrs={'class':'WB_text', 'node-type' : 'feed_list_content'})

            return text
            #self.writefile('text1.txt',text)           
            #self.writefile('./output/result1',eval("u'''"+text+"'''"))
            
    def get_secondpage(self,url):
            getWeiboPage.body['count'] = '15'
            getWeiboPage.body['pagebar'] = '0'
            getWeiboPage.body['pre_page'] = getWeiboPage.body['page']

            url = url +'?'+ urllib.urlencode(getWeiboPage.body1)+'&'+ urllib.urlencode(getWeiboPage.body)
            req = urllib2.Request(url)
            result = urllib2.urlopen(req)
            page = result.read()
            soup = parse_followings(page)
            text = soup.findAll('div', attrs={'class':'WB_text', 'node-type' : 'feed_list_content'})
            return text 
            #self.writefile('text2.txt',text)           
            #self.writefile('./output/result2',eval("u'''"+text+"'''"))
            
    def get_thirdpage(self,url):
            getWeiboPage.body['count'] = '15'
            getWeiboPage.body['pagebar'] = '1'
            getWeiboPage.body['pre_page'] = getWeiboPage.body['page']

            url = url + '?'+ urllib.urlencode(getWeiboPage.body1)+'&'+ urllib.urlencode(getWeiboPage.body)
            req = urllib2.Request(url)
            result = urllib2.urlopen(req)
            page = result.read()
            soup = parse_followings(page)
            text = soup.findAll('div', attrs={'class':'WB_text', 'node-type' : 'feed_list_content'})

            return text
            #self.writefile('text3.txt',text)           
            #self.writefile('./output/result3',eval("u'''"+text+"'''"))
               
    def get_url(self,uid):
            url = 'http://www.weibo.com/p/'+ str(uid)+ "/weibo"
            return url

    def writefile(self,filename,content):
            fw = open(filename,'w')
            fw.write(content)
            fw.close()
