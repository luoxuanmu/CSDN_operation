#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 13:46
# @Author  : luoxuan
# @File    : test.py
import requests
import  json


def blog(user_name):
    '''
    获取指定CSDN用户发布的所有博文的地址
    :param user_name: CSDN账号的用户名
    :return:
    '''
    tag = 1
    page_num = 1
    while tag:
        url = 'https://blog.csdn.net/community/home-api/v1/get-business-list?page={}&size=20&businessType=blog' \
              '&orderby=&noMore=false&year=&month=&username={}'.format(page_num,user_name)
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
        res = requests.get(url=url, timeout=20, headers=header)
        html_info = json.loads(res.text)
        result = html_info['data']['list']
        for i in result:
            url1 = i['url']
            with open('url_list.txt', 'a', encoding='utf-8') as f:
                f.write(url1+'\n')
        print('第{}页数据采集且写入文件成功'.format(page_num))
        if len(result) >= 20:
            page_num += 1
        else:
            tag = 0


if __name__ == '__main__':
    user_name = '你CSDN账号的用户名'
    blog(user_name)