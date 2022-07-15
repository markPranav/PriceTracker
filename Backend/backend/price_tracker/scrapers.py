import re
from bs4 import BeautifulSoup
import requests

def wooCommerce(url):
  pass

def mdComputers(url):
  pass

def vishalPeripherals(url):
  pass

def genericScrapper(url):
  page = requests.get(url, timeout=2)
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