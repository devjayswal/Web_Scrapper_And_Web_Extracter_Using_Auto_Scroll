url = "https://www.zomato.com/lucknow/delivery-in-charbagh?dishv2_id=55280"

path_to_file = r"/home/era/Desktop/Work/"

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup

mode = "" #mode=extract/scrape/""

if(mode != "extract"):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(url)

    last_height = 0

    while True:
        driver.execute_script('window.scrollBy(0, 5000)')
        time.sleep(10)

        new_height = driver.execute_script("return document.body.scrollHeight")
        print(str(new_height)+"-"+str(last_height))

        if(new_height == last_height):
            break

        else:
            last_height = new_height

    page_source = driver.page_source

    f = open(path_to_file+"source.txt","a",encoding="utf-8")
    f.write(page_source)
    f.close()


if(mode != "scrape"):
    data = []

    f = open(path_to_file+"source.txt","r",encoding="utf-8")
    page_source = f.read()
    f.close()

    soup = BeautifulSoup(page_source,features="lxml")

    items = soup.find_all("a",class_="sc-btewqU dlikcC")

    for item in items:
        item_out = {}

        # Extract the title (name)
        title = item.find("h4", class_="sc-1hp8d8a-0 eKNGxQ")
        item_out['Title'] = title.text if title else None

        # Extract the link
        item_out['Link'] = item.attrs['href']

        # Extract the rating
        rating = item.find("div", class_="sc-1q7bklc-5 hKSxpS")
        item_out['Rating'] = rating.text if rating else None

        # Extract the description (tags)
        description = item.find("p", class_="sc-1hez2tp-0 sc-bYSrVf gSYfM")
        item_out['Description'] = description.text if description else None

        # Extract the price
        price = item.find("p", class_="sc-1hez2tp-0 iXSVFy irdj6p")
        item_out['Price'] = price.text if price else None

        # Extract the time
        time = item.find("span", class_="sc-iOVSdP kUbhmr")
        item_out['Time'] = time.text if time else None

        data.append(item_out)

df = pd.DataFrame(data)
df.to_excel(path_to_file+"startups.xlsx")
df.to_csv(path_to_file+"startups.csv",sep=";",index=False)