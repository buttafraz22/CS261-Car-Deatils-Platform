# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 11:04:23 2022

@author: HP
"""
"total count of pages in the website for scraping the pakwheels ads"

import requests
# import pandas as pd
from bs4 import BeautifulSoup


# import urllib.request
START = 1
END = 10
all_data = []
millege = []
cc = []

# base_url = "https://www.pakwheels.com/used-cars/search/-/?_pjax=%5Bdata-pjax-container%5D"
# soup = BeautifulSoup(requests.get(base_url).content, "html.parser")

# for ul in soup.select("ul.search-pagi"):
#         info = [i['href'] for i in ul.find_all('a', href=True)]
# value = info[7]
# print(value)
# END=int(value[58:len(value)])

def get_words_in_page(url):
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    
    for ul in soup.select("ul.search-vehicle-info-2"):
            url = ul.find_previous('a').get('href')
            url = 'https://www.pakwheels.com/'+url
            car_name = ul.find_previous("h3").get_text(strip=True)
            info = [li.get_text(strip=True) for li in ul.select("li")]
            data = info[1]
            for i in range(0,len(data)):
                millege.append(data[:-3].replace(',',''))
            for i in range(0,len(millege)):
                info[1] = millege[i]
            data = info[3]
            for i in range(0,len(data)):
                cc.append(data[:-3])
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

