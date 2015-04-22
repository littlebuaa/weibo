#!/usr/bin/env python
#coding=utf-8

'''Author: Houkai
DATE: 2013.12.23'''

import urllib.request, urllib.parse, urllib.error
import base64
import rsa
import binascii

def PostEncode(userName, passWord, serverTime, nonce, pubkey, rsakv):
    "Used to generate POST data"
        
    encodedUserName = GetUserName(userName)#用户名使用base64加密
    encodedPassWord = get_pwd(passWord, serverTime, nonce, pubkey)#目前密码采用rsa加密
    postPara = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'userticket': '1',
        #'ssosimplelogin': '1',
        'vsnf': '1',
        'vsnval': '',
        'su': encodedUserName,
        'service': 'miniblog',
        'servertime': serverTime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'sp': encodedPassWord,
        'sr' :'1536*864',
        'encoding': 'UTF-8',
        'prelt': '827',
        'rsakv': rsakv,
        'url': 'http://www.weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META'
    }
    postData = urllib.parse.urlencode(postPara)#网络编码
    postData = postData.encode('utf-8')
    return postData


def GetUserName(userName):
    "Used to encode user name"
    
    userNameTemp = urllib.parse.quote(userName)
    userNameEncoded = base64.encodestring(userNameTemp.encode())[:-1]
    return userNameEncoded


def get_pwd(password, servertime, nonce, pubkey):
    rsaPublickey = int(pubkey, 16)
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(password) #拼接明文js加密文件中得到
    passwd = rsa.encrypt(message.encode(), key) #加密
    passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。
    return passwd

### Postdata exemple
'''
entry=weibo
gateway=1
from=
savestate=7
useticket=1
pagerefer=
vsnf=1
su=bGl0dW9idWFhJTQwaG90bWFpbC5jb20%3D
service=miniblog
servertime=1429028279
nonce=39CLV6
pwencode=rsa2
rsakv=1330428213
sp=8a478a82d8fea84863798620cec9457e035ebd228f2e9fc284990d41578940d82697895d0f414aeec768ff41072a66d7fe286029b731c7d653fd993c82830886b06735a698302a2cd793fa27d91eec138ca7b20a40ddef689f74e78d0839eb885dbf11d1beb62f9a0e3447d7cdcc76ff4152404ad3ca30c111417ebf27252f82
sr=1536*864
encoding=UTF-8
prelt=827
url=http%3A%2F%2Fwww.weibo.com%2Fajaxlogin.php%3Fframelogin%3D1%26callback%3Dparent.sinaSSOController.feedBackUrlCallBack
returntype=META

'''
    