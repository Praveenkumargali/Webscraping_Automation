# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://www.goodbasket.com/en/vegetables"

page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
VegNames = []
Price=[]


for i in soup.findAll('div', attrs={'class':'product details slider-product-item-details'}):
    name=i.a['title']
    amount=i.find('span', attrs={'class': 'price'})
    VegNames.append(name)
    amount= amount.text
    amount=amount.replace("AED","")
    Price.append(amount)
    
df = pd.DataFrame({'Product Name':VegNames,'Price in AED':Price}) 
df.to_csv('products_goodbasket.csv', index=False, encoding='utf-8')
    