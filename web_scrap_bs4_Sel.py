# Dependencies
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import numpy as np


# intial variables
url = 'https://www.bing.com/travel/hotel-search?q=hotels+in+bangkok%2C+thailand&loc=bangkok%2C+thailand&cin=2023-01-02&cout=2023-01-03&guests=2A0C&age=&displaytext=&id=&index=0&form=UNKHUB&type=hotel&minprice=undefined&maxprice=undefined&entrypoint=UNKHUB&sort=HotelPriceAsc'


ser = Service("Instagram_fame_trend\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get(url)

# wait for 10 sec before taking any action so website can load
time.sleep(5)

# get html response
loginBtn = driver.find_element(By.CLASS_NAME, "HotelsListItem ")

print(loginBtn.text)


# %% Different ways to get the values


# to get price alone -use xpath and not element:
# remember that to get multiple prie loop through all the element/hotels in the page in bing there will be 25 items so we are looping
# through 25 elements except 3 since it is little different
ad_element = 1
total_hotel = 25
# we are adding +1 since the last number will be excluded in np
hotel_per_page = np.arange(1, total_hotel+ad_element+1)
# we have 1 to 25 except 3 which is in 3th index
hotel_per_page = np.delete(hotel_per_page, 2)

# METHOD 1 - THORUGH XPATH
for hotel_num in hotel_per_page:
    print(hotel_num, '\t', driver.find_element(
        By.XPATH, f'//*[@id="main"]/div/div[3]/div/div/div[{hotel_num}]/div[2]/div[2]/div/div/div').text)


# METHOD 2 - THORUGH class name and find elements
# Analysing the html we found time property-name comes 1st and inside that offered-price will be there so
# so we will
t0 = time.time()

hotel_list = []
price_list = []
review_list = []
inds = 0
for hotel_name_price in driver.find_elements(By.XPATH, "//*[@class='property-name' or @class='info-rating' or @class='offered-price']"):
    if inds == 0:
        # print('Hotel: ', hotel_name_price.text)
        price_list.append(hotel_name_price.text)
        inds = inds+1
    elif inds == 1:
        # print('Review: ', hotel_name_price.text)
        review_list.append(hotel_name_price.text)
        inds = inds+1
    elif inds == 2:
        # print('price: ', hotel_name_price.text)
        hotel_list.append(hotel_name_price.text)
        inds = 0

t1 = time.time()
print(f'Total time:', t1-t0)


# For hotels in bing
# https://www.bing.com/travel/hotel-search?q=<city>%2C+<country>

# https://www.bing.com/travel/hotel-search?q=hotels+in+bangkok%2C+thailand&loc=bangkok%2C+thailand&cin=2023-01-02&cout=2023-01-03&guests=2A0C&age=&displaytext=&id=&index=75&form=UNKHUB&type=hotel&minprice=undefined&maxprice=undefined&entrypoint=UNKHUB&sort=HotelPriceAsc
