# -*- coding: utf-8 -*-
from multiprocessing import Pool
from get_parsing import get_item_info,get_links_from,url_list,item_info
db_urls=[item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x-y
if __name__ == '__main__':
    pool = Pool()
    # pool = Pool()
    pool.map(get_item_info,rest_of_urls)
    pool.close()
    pool.join()
