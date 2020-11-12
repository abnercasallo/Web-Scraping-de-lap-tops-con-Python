# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#from BeautifulSoup import BeautifulSoup
#gedit web-s.py
#Primero hemos instalado request es el terminal
#Tmb beautiful soup:$ pip3 install beautifulsoup4
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#prices=[]
#driver.get("https://hiraoka.com.pe/tecnologia/computadoras/laptops")
#content = driver.page_source
#soup = BeautifulSoup(content)
    

import requests

URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
prices_t = soup.find_all('span', class_ = "price")
prices_text=[item.text for item in prices_t]
print(prices_text)



#int(3,399.00.replace(',',''))

text2=[]
for i in prices_text:
    a=i.replace(',','')
    b=a.replace('S/ ','')
    c=b.replace('.00','')
    text2.append(c)
    
num_prices_1=[]
for a in text2:
    num_prices_1.append(int(a))
       
print(num_prices_1)

#AVERAGE:
total_pag1=0
for i in num_prices_1:
    total_pag1=total_pag1+i
print(total_pag1)

av_price_pag1=total_pag1/len(num_prices_1)
print(av_price_pag1)

#########AHORA HACER UN BUCLE PARA TODAS LAS PÁGINAS CON FOR
#prices_text=[]
prices=[]
for i in range(1,5):#1,2,3,4
    if i==1:
        URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        prices_t = soup.find_all('span', class_ = "price")
        prices_text=[item.text for item in prices_t]
        for i in prices_text:
                a=i.replace(',','')
                b=a.replace('S/ ','')
                c=b.replace('.00','')
                prices.append(int(c))
    else:
        a=str(i)
        URL = 'https://hiraoka.com.pe/tecnologia/computadoras/laptops'+'?p='+a
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        prices_t = soup.find_all('span', class_ = "price")
        prices_text=[item.text for item in prices_t]
        for i in prices_text:
            a=i.replace(',','')
            b=a.replace('S/ ','')
            c=b.replace('.00','')
            prices.append(int(c))


print(prices)

#ARMAMOS EL DATA FRAME
df_11nov = pd.DataFrame(prices, columns =['Precios al 12/11/2020']) 
print(df_11nov)
df_11nov.to_csv(r'D:\Git Hub-BEST\Web-Scraping-de-lap-tops-con-Python\Data generada\12 de nov.csv',
                sep=';')
#TOTAL LIST, UNMOS LA LISTA DE LA PÁGINA 1 AL DE LA 2 A LA 4:
#SI NO SE INCLUYÓ A LA LISTA
#num_total_prices.append(num_prices_1)
    

        
    
    
