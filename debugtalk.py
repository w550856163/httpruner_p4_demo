#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: debugtalk.py
# @time: 2020/11/4 8:30 下午

import random
import requests
def get_search_word():
    word_list = ['newdream','12306','火车票','新梦想软测教育']
    num = random.randint(0,len(word_list)-1)
    return word_list[num]

def get_access_token():
    p_dict = {
        'grant_type': 'client_credential',
        'appid': 'wx55614004f367f8ca',
        'secret': '65515b46dd758dfdb09420bb7db2c67f'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=p_dict)
        token = response.json()['access_token']
    except KeyError as e:
        token = None
    return token

if __name__=='__main__':
    print( get_access_token()  )

'''
def get_search_word():
    word_list = ['newdream','12306','火车票','新梦想软测教育']
    num = random.randint(0,len(word_list)-1)
    return word_list[num]

def s():
    print( '测试用例开始执行' )
def t():
    print('测试用例结束执行')

def s1(step_name):   #传参
    print( '测试步骤 [%s] 开始执行'%step_name )
def t1(step_name):
    print('测试步骤 [%s] 结束执行'%step_name)

def get_true():
    return None

def get_access_token():
    p_dict = {
        'grant_type': 'client_credential',
        'appid': 'wx55614004f367f8',  #ca 去掉 错误的appid
        'secret': '65515b46dd758dfdb09420bb7db2c67f'
    }
    try:
        response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token',
                                params=p_dict)
        token = response.json()['access_token']
    except KeyError as e:
        token = None
    return token
if __name__=='__main__':
    print( get_access_token())  
  '''

