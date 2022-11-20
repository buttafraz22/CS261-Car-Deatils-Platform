# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 09:46:06 2022

@author: HP
"""

import requests
# import pandas as pd
from bs4 import BeautifulSoup
# from app import Worker as w
# import urllib.request
START = 1
END = 10
all_data = []
year = []
millege = []
cc = []

def get_words_in_page(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    for ul in soup.select("div.e181zu8w1"):
            url = ul.find_previous('a').get('href')
            url = 'https://carvago.com/'+url
            car_name = ul.find_previous("h6").get_text(strip=True)
            info = [li.get_text(strip=True) for li in ul.select("div.e1me6z3j2")]
            data = info[0]
            info[0] = info[1]
            info[1] = data
            data = info[3]
            info[3] = info[4]
            info[4] = data
            data = info[2]
            info[2] = info[3]
            info[3] = data
            data = info[0]
            for i in range(0,len(data)):
                year.append(data[-4:])
            for i in range(0,len(year)):
                info[0] = year[i]
            data = info[1]
            for i in range(0,len(data)):
                millege.append(data[:-3].replace(u'\xa0', u''))
            for i in range(0,len(millege)):
                info[1] = millege[i]
            data = info[3]
            for i in range(0,len(data)):
                cc.append(int(data[:-2])*15)
            for i in range(0,len(cc)):
                info[3] = cc[i]
            try:
                data = info[5]
                for i in range(0,len(data)):
                    info[5] = data[:1]
                all_data.append([car_name, url,*info])
            except:
                all_data.append([car_name, url,*info])
    return all_data






