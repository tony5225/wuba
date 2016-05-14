# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import random
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
         'Connection':'keep-alive'}
proxy_list=['http://190.147.220.37:8080','http://194.79.146.210:8080','http://213.6.3.35:8080','http://223.27.170.219:10000','http://31.208.7.22:8888','http://136.243.122.90:3128']
'''proxy_list = [
    'http://117.177.250.151:8081',
    'http://111.85.219.250:3129',
    'http://122.70.183.138:8118',
    ]'''

start_url='http://bj.ganji.com/wu/'
host_url='http://bj.ganji.com'
urls=[]
'''proxy_ip=random.choice(proxy_list)
proxies = {'http': proxy_ip}'''
def get_links(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links1=soup.select('dt > a')
    links2=soup.select('dd > a')
    links=links1+links2
    for link in links:
        page_url=host_url+link.get('href')
        print page_url
        urls.append(page_url)
    return urls
linkurl=get_links(start_url)
