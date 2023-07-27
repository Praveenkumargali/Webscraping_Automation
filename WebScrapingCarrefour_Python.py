
#import libraries
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


try:
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    }
    response = requests.get("https://www.carrefouruae.com/mafuae/en/fresh-food/fruits-vegetables/vegetables/c/F11660500", headers=headers, timeout=5)

    if response.status_code != 200:
        print("error!")
    else:
        print(response.status_code)
except requests.exceptions.Timeout as error:
    print('time out')


#Variable Initializing
Page = response.text
j=1
prodStart = "\"altText\":\""
ProdEnd = "\""

PriceStart = "\"originalPrice\":"
PriceEnd = ","  
Vegetables = []

#Using string operations based on the pattern in page response text
temp = (Page.split(prodStart))[1].split(ProdEnd)[0]
for i in range(1,1000):
    try:
      Veg = (Page.split(prodStart))[i].split(ProdEnd)[0]
    except IndexError:
      break
    #saving the Product and price in "product_Price format"
    if Veg != temp:
        Price = (Page.split(PriceStart))[j].split(PriceEnd)[0]
        Vegetables.append(Veg + "_"+ Price)
        j=j+1
        temp = Veg

Product = []
Amount = []

#Separate the Vegetables and Price   
for i in Vegetables:
    j = i.split("_")
    Product.append(j[0])
    Amount.append(j[1])
#place the product and price in csv    
df = pd.DataFrame({'Product Name':Product,'Price in AED':Amount}) 
df.to_csv('products_Carrefour.csv', index=False, encoding='utf-8')  
    
    
