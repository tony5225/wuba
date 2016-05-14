# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from get_parsing import url_list
import pymongo
conn = pymongo.MongoClient(host='127.0.0.1',port=27017)
db = conn.ganji

#account = db
print db.collection_names()
print db.url_listganji.count()
print db.item_infoganji.count()