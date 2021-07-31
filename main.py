import pandas as pd
from selenium import webdriver
import streamlit as st
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
import plotly.express as px


product = st.text_input('Enter The Product')

with st.spinner("Loading Data..."):
    st.markdown("""
        <style>
            .mainhead{
                font-family: Courgette ,Book Antiqua ;
                #letter-spacing:.1px;
                word-spacing:1px;
                color :#4acaff; 
                text-shadow: 1px -1px 1px white, 1px -1px 2px white;
                font-size:40px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .detail{
                font-size:18px;
                letter-spacing:.1px;
                word-spacing:1px;
                font-family:Calibri;
                color:#3574cb;
                display:inline-block;
                }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 class="mainhead">Price Comparision Of Product </h1> <img src="" />',
                unsafe_allow_html=True)
    col1, col2 = st.beta_columns([5, 10])

    with col1:

        st.image('https://media.giphy.com/media/5k1Wu87CzkDfrx0Xwj/giphy.gif')

    with col2:

        col = st.beta_container()

        with col:
            st.markdown("""
                <style>
                    .content{
                    margin-top: 0%;
                    letter-spacing:.1px;
                    word-spacing:1px;
                    color:indianred;
                    margin-left:5%;}
                </style>
            """, unsafe_allow_html=True)

            st.markdown('<p class="content">Hello <br> Welcome To My Project:- Price Comparision Of Product. In this Web scraping with Python, the script searches for a specified product via URL and find out the price at that moment. This is particularly useful when you want to monitor the price of the specific item from eCommerce platforms. Here, in this program, we have targeted two major eCommerce website (Flipkart and Amazon) to find the price of a product. On each execution, Both websites are crawled and the price is obtained.The price of the same product from all the sources are displayed on the console window, so that buyer can see the prices and make the decision to buy from the platform which offers the lowest price! </p>', unsafe_allow_html=True)
            st.markdown(
                '<marquee class="content" style = "float:right;"> Made By Vaibhav Shrimali</marquee>', unsafe_allow_html=True)

st.markdown("")
st.markdown("___")


#-------------------------------------------Scraping of price From Amazon and Flipkart--------------------------------------#
if product:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    l=product
    r="https://www.amazon.in/s?k="
    url =r+l
    driver.get(url)
    time.sleep(2)
    
    main_area = driver.find_element_by_css_selector("div.s-main-slot.s-result-list.s-search-results.sg-row")

    price = main_area.find_elements_by_css_selector('span.a-price-whole')
    data1 = []
    for a in price:
        data1.append({
        
        'price':a.text})

        pd.DataFrame(data1).to_csv("Amazon_price.csv")
        da= pd.read_csv("Amazon_price.csv")
        
        #-------------------------Cleaning Price value-------------------------------------#
        da['price'] = da['price'].replace({'₹': '', ',': '', '\(': '-', '\)': ''}, regex=True).astype(float)

        pd.DataFrame(da).to_csv("Amazon_price.csv"  )



    r="https://www.flipkart.com/search?q="
    url =r+l
    
    driver.get(url)
    time.sleep(2)
    main_area = driver.find_element_by_css_selector("div._36fx1h._6t1WkM._3HqJxg")
    print(main_area)
    price = main_area.find_elements_by_css_selector('div._30jeq3')
    data2 = []   
    for a in price:
        data2.append({
        
        'price':a.text})

    pd.DataFrame(data2).to_csv("flipkart_price.csv")
    df= pd.read_csv("Flipkart_price.csv")

    df['price'] = df['price'].replace({'₹': '', ',': '', '\(': '-', '\)': ''}, regex=True).astype(float)
    pd.DataFrame(df).to_csv("Flipkart_price.csv")
    



#-------------------------------------MainPage fro Streamlit--------------------------------------------#

    
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
    

    st.sidebar.header("Price Comparision of Product between Amazon and Flipkart")
    st.sidebar.image("https://media.giphy.com/media/SpopD7IQN2gK3qN4jS/giphy.gif", width=300)

    option=st.sidebar.selectbox("Choose any option",['Cheapest','costliest'])

    da= pd.read_csv('Amazon_price.csv')
    df= pd.read_csv("Flipkart_price.csv")
    if option == 'Cheapest':
        st.header('Cheapest Product Price is')
        st.success("Cheapest Price is on Amazon is")
        r=da['price'].min()
        st.error(r)
        st.success('Cheapest price on Flipkart is:-')
        s=df['price'].min()
        st.error(s)  

    if option == 'costliest':
        st.header("Costliest Product Price is")
        st.success('Costliest price on Amazon is:-')
        p = da['price'].max()
        st.error(p)
        st.success('Costliest price on Flipkart is:-')
        q = df['price'].max()
        st.error(q)

    st.markdown(
                '<marquee class="content" style = "float:right;"> Visit My gitHub:- https://github.com/vaibhavs9894</marquee>', unsafe_allow_html=True)


