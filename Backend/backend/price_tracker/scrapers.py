import re
from time import sleep
from bs4 import BeautifulSoup
import requests

def wooCommerce(url):
  pass

def mdComputers(url):
  pass

def vishalPeripherals(url):
  pass

def genericScrapper(url): 
  headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
       "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
       "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
  page = requests.get(url, timeout=2,headers=headers)
  if(page.status_code in [403, 503]):
    from selenium import webdriver
    import os

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    print(driver)
    driver.get(url)
    sleep(10)
    print(driver.title)
    raise Exception("Bot detected")
  soup = BeautifulSoup(page.content, 'html.parser')
  
  if(soup.find(class_=re.compile("woocommerce"))):
      price_el = soup.find('p',class_=re.compile("price")).getText().split()
      stock = soup.find(class_=re.compile("stock-availability"))
      if(not stock):
        stock = True
      else:  
        stock = "in stock" in stock.get_text().lower()
  else:
      price_el = [soup.find(class_=re.compile("price-new")).getText().strip(), soup.find(class_=re.compile("price-old")).getText().strip()]
      stock = soup.find(class_=re.compile("stock")).get_text().lower()
      stock = "in stock" in stock
  
  price_el = list(map(lambda x: float(re.sub(r'[^\d.]', '', x)), price_el))
  price_el.sort()
  price_el.append(stock)
  return price_el