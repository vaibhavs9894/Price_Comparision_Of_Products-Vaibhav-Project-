import pandas as pd
from selenium import webdriver
import requests
import streamlit as st
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
import plotly.express as px

st.set_page_config(page_title='Price Comparision of Product')
driver = webdriver.Chrome(ChromeDriverManager().install())

path = st.text_input('Enter The Product')

l=path
r="https://www.amazon.in/s?k="
url =r+l
driver.get(url)
time.sleep(2)
    
main_area = driver.find_element_by_css_selector("div.s-main-slot.s-result-list.s-search-results.sg-row")

price = main_area.find_elements_by_css_selector('span.a-price-whole')
data = []
for a in price:
    data.append({
        
    'price':a.text})

    pd.DataFrame(data).to_csv("Amazon_price.csv")
    da= pd.read_csv("Amazon_price.csv")

    da['price'] = da['price'].replace({'₹': '', ',': '', '\(': '-', '\)': ''}, regex=True).astype(float)

    pd.DataFrame(da).to_csv("Amazon_price.csv"  )

#-------------------------------------------Scraping--------------------------------------#

r="https://www.flipkart.com/search?q="
url =r+l
driver.get(url)
time.sleep(2)
main_area = driver.find_element_by_css_selector("div._36fx1h._6t1WkM._3HqJxg")
print(main_area)
price = main_area.find_elements_by_css_selector('div._30jeq3')
data = []   
for a in price:
    data.append({
        
    'price':a.text})

pd.DataFrame(data).to_csv("flipkart_price.csv")
df= pd.read_csv("Flipkart_price.csv")

df['price'] = df['price'].replace({'₹': '', ',': '', '\(': '-', '\)': ''}, regex=True).astype(float)
pd.DataFrame(df).to_csv("Flipkart_price.csv")

#-------------------------------------MainPage fro Streamlit--------------------------------------------#



st.sidebar.header("Compare Product between Amazon and Flipkart")
st.sidebar.image("https://media.giphy.com/media/SpopD7IQN2gK3qN4jS/giphy.gif", width=300)

st.info('Price Scrap from Flipkart are:-')
img = Image.open("flipkart-trans.png")
st.image(img, width=200)
df = pd.read_csv('Flipkart_price.csv')
st.write(df.head(50))

st.info('Price Scrap from Amazon are:-')
img = Image.open("amazon-trans.png")
st.image(img, width=200)
da= pd.read_csv('Amazon_price.csv')
st.write(da.head(50))

option=st.sidebar.selectbox("Choose any option",['costliest','Cheapest'])

if option == 'costliest':
    st.header("Costliest Product Price is")
    st.write('Costliest price on Amazon is:-')
    p = da['price'].max()
    st.success(p)
    st.write('Costliest price on Flipkart is:-')
    q = df['price'].max()
    st.success(q)

if option == 'Cheapest':
    st.header('Cheapest Product Price is')
    st.header("Costliest Product Price is")
    st.write('Cheapest price on Amazon is:-')
    r=da['price'].min()
    st.success(r)
    st.write('Cheapest price on Flipkart is:-')
    s=df['price'].min()
    st.success(s)  


if(st.button("Feeling Lucky")):
    st.image("https://media.giphy.com/media/fUYhyT9IjftxrxJXcE/giphy.gif", width=300)