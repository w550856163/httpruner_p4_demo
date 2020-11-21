#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: debugtalk.py
# @time: 2020/11/4 8:30 下午
import os
import random
import requests
from faker import Faker
import pymysql

# #设置代理
# os.environ['http_proxy'] = 'http://127.0.0.1:0000'
# os.environ['https_proxy'] = 'https://127.0.0.1:0000'


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

# 参数实战：
def get_params01():
    return ['newdream','12306','火车票']
def get_params02():
    return [['newdream','newdream_百度搜索'],['12306','12306_百度搜索'],['火车票','火车票_百度搜索']]
def get_random_int(min,max,count=3): #标记1
    num_list = []
    for i in range(count): #i取值0，1，2，循环3次
        num_list.append( random.randint(min,max) )
    return num_list

def get_random_string(base_str,str_len,count=3):#标记2
    #base_str = base_str +'!@#$'  #处理特殊字符
    string_list = []
    for i in range(count):
        string = ''
        for j in range(int(str_len)):#标记3, int(str_len) 强制转换为整型
            string = string + base_str[random.randint(0,len(base_str)-1)] #base_str取一个随机数
        string_list.append(string)#循环生成的3个随机字符串3次加到list去
    return string_list

#def get_random_phonenum(mobile_num,count=3):#标记5
def get_random_phonenum(*mobile_num, count=3):  # 标记6
    phonenum_list = []
    for i in range(count):
        phone_start = str(random.choice(mobile_num)) #strtestsuite05 标记7 int->str
        phone_end = ''.join( random.sample('0123456789',8) )
        phonenum_list.append( phone_start + phone_end )  #强转 str +str
    return phonenum_list


def get_random_name(count=3): #标记8,testsuit-05执行
    f = Faker(locale='zh_CN')
    name_list = []
    for i in range(count):
        name_list.append( f.name() )
    return name_list

def get_params_by_mysql(case_name):
    mysql_connect = pymysql.connect(host='localhost', port=3306,
                                    user='root', password='123456',
                                    database='api', charset='utf8')
    cur = mysql_connect.cursor()
    cur.execute("select test_data,excepted_result from test_data where case_name like '%s%%';"%case_name)
    case_data = cur.fetchall()
    cur.close()
    mysql_connect.close()

    list_case_data = list(case_data) #外层强转为列表
    for i in range(len(list_case_data)): #里层每一个强转为列表
        list_case_data[i] = list(list_case_data[i])
    return list_case_data

def to_ISO_8859_1(str):
    return str.encode('utf8').decode('iso8859-1')
def to_UTF_8(str):
    return str.encode('iso8859-1').decode('utf8')

#if __name__=='__main__':
   #print(get_random_phonenum(['131', '132', '133']))# 标记5
   #print( get_random_phonenum('131','132')  ) #标记6

    #print(get_random_int(0,1000))#标记1
    #print(get_random_int(0, 1000,10))  # 标记1,10个随机数

# #例：command+ / 批量注释
#     str1 = '1234567890abcdefghi中国我们'
#     # # 需求：上述的字符串为底，用它们的字母组合生成随机字符串
#     print(str1[9])    #结果：0
#     print(len(str1))    #结果：23
#     print( str1[random.randint(0,len(str1)-1)] )#从0-22随机取一个数
#     str2 = ''
#     for i in range(10):#取出10个随机字符进行累增       #标记3
#         str2 = str2 + str1[random.randint(0,len(str1)-1)]
#     print(str2)

    # #需求：实现随机手机号 131  132  133
    # mobile_num = ['131','132','133']
    # print( random.choice(mobile_num) )
    # # 131 0123456789 == 8
    # print( random.sample('0123456789',8) )
    # a = ['5', '0', '8', '6', '4', '3', '7', '2']
    # print( random.choice(mobile_num) + ''.join( a ) ) #列表转换成字符串

   # print(get_random_string('sdhjjre@#$$',9))#标记2
    # print(get_random_string('123456abcdef',6)) #testsuite_demo_05.yml 标记4

if __name__ == '__main__':
    print(get_params_by_mysql('test_baidu_search')) #测试get_params_by_mysql函数

   #  mysql_connect = pymysql.connect(host='localhost',port=3306,
   #                                  user='root',password='123456',
   #                                  database='api',charset='utf8')
   #  #cur = mysql_connect.cursor(cursor=pymysql.cursors.DictCursor) #默认元组类型数据 ，返回字典类型 #标记9
   #  cur = mysql_connect.cursor() #不转字典，返回元祖
   #  #cur.execute('select * from  test_data')  #标记9
   #
   #  cur.execute("select test_data,excepted_result from test_data where case_name like '%s%%';"%'test_baidu_search')
   # # print( cur.fetchone() )#不管查询结果是多条数据还是单条数据，使用fetchone得到的始终是一个元组，默认是结果中的第一条数据构成的元组
   #  print( cur.fetchall() )#获取所有数据，不管查询结果是多条数据还是单条数据，使用fetchall得到的始终是一个由元组组成的列表。
   #  cur.close()
   #  mysql_connect.close()
