# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import pymongo
import time
import json
import random
client=pymongo.MongoClient('localhost',27017)
ganji=client['ganji']
url_list=ganji['url_listganji']
item_info=ganji['item_infoganji']
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36',
         'Connection':'keep-alive'}
#proxy_list=['http://190.147.220.37:8080','http://194.79.146.210:8080','http://213.6.3.35:8080','http://223.27.170.219:10000','http://31.208.7.22:8888','http://136.243.122.90:3128']
proxy_list = [
    'http://45.79.101.62:3128',
    'http://108.59.10.138:55555',
    'http://114.130.43.49:80',
    ]
proxy_ip=random.choice(proxy_list)
proxies = {'http': proxy_ip}
def get_links_from(url,page=1):
    url1=url+'o%s/'%(str(page))
    wb_data=requests.get(url1,headers=headers,proxies=proxies)
    soup=BeautifulSoup(wb_data.text,'lxml')
#   http://bj.ganji.com/jiaju/1983801931x.htm
    link_id=soup.select('li.js-item')
    for id in link_id:
        link=url+id.get('data-puid')+'x.htm'
        url_list.insert_one({'url':link})
        print link


def get_item_info(url):
    if 'zhuanzhuan' in url:
        pass
    else:
        wb_data=requests.get(url,headers=headers)
        soup=BeautifulSoup(wb_data.text,'lxml')
        if wb_data.status_code == 404 :
            pass
        else:
            try:
                url=url
                title=soup.title.text.strip()
                type=list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings)
                price=soup.find_all('i',class_='f22 fc-orange f-type')[0].text if soup.find_all('i',class_='f22 fc-orange f-type') else None
                qtime=soup.select('i.pr-5')[0].text.strip().split('&')[0] if soup.find_all('i',class_='pr-5') else None
                location=list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a')))
                data={'title':title,'price':price,'type':type,'location':location,'url':url,'time':qtime}
            #        item_info.insert_one(data)
                item_info.insert_one(data)

                print data
            except IndexError:
                print url
                print "indexerror"
#get_item_info('http://bj.ganji.com/shuma/2009330004x.htm')