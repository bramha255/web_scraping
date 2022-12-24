#$$ Dependencies

#Webscraper
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests

# Extras 
import pandas as pd
import time

# For handling exception error when the site reaches last page
from selenium.common.exceptions import TimeoutException

#%% intial setups
url = <enter_website_url>


ser = Service("Web_scraping\chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)
driver.get(url)

# Looping through all the pages and scraping the details
contents = []
while True:
    try:
        #after the webpage starts wait
        time.sleep(5)
        
        #get the next button's link using beautifulsoup and replace the old url(1st page) with the new one
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')
        next_button = soup.find('a', class_="_1bfat5l").get('href') #next button has class "_1bfat5l"
        next_button = "https://www.website.co.in" + next_button
        url = next_button
        
        #get all the html content from the webpage in single shot
        contents.append(driver.page_source)
        
        #wait till the next page loads and click
        wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[aria-label^='Next']")))
        wait.click() 
        
    except TimeoutException:
        #if next button is not found then the WebDriverWait will throw a TimeoutException error this is to handle it
        print('End of the page')
        break
        driver.close()

#%% Extracting the required hotel information from the scraped data

links_list = []
hotel_list = []
price_list = []
review_list = []

for content in contents:
    
    #indicator of begining of a page comment it during run
    print('======================================================\
          ======================================================\
          ====================NEW Page==========================\
          ======================================================')
    
    # from the html scraped, use beautifulsoup to extract each data using their class
    soup = BeautifulSoup(content, 'html.parser')
    posts = soup.find_all('div', class_="c4mnd7m dir dir-ltr")
    
    for (num, post) in enumerate(posts):
      links = post.find('meta', {'itemprop':"url"}).get('content')
      links_list.append(links)
      
      name = post.find('span', class_="t6mzqp7 dir dir-ltr")
      hotel_list.append(name.text)
      
      price = post.find('span', class_="a8jt5op dir dir-ltr")
      price_list.append(price.text)
      
      review = post.find('span', class_="t5eq1io r4a59j5 dir dir-ltr")
      if review != None:
          review_list.append(review.get('aria-label'))   #from the span tag get only the "aria-label" which has the review
      else:
          review_list.append('No Review')
          
      print(f"Hotel: {hotel_list[-1]} Review: {review_list[-1]}, link: {links_list[-1]}",'\n')


# %% Converting extracted values to csv(our option but there are other ways to convert it as well)

df = pd.DataFrame({'Hotels': hotel_list, 'Link': links_list,
                  'Price': price_list, 'Reviews': review_list})

df.to_csv('Hotel.csv', index=False, header=True)
