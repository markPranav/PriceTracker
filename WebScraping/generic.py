import re
from bs4 import BeautifulSoup
import requests

# url = "https://mdcomputers.in/asus-rog-strix-rtx3070ti-o8g-gaming.html"
# url = "https://www.vishalperipherals.in/colorful-igame-geforce-rtx3070ti-ultra-w-oc-8g-v?manufacturer_id=94"
# url = "https://www.easyshoppi.com/product/igame-geforce-rtx-3070-ti-ultra-w-oc-8g-v/"
url = "https://www.easyshoppi.com/product/intel-core-i9-12900k-3-2-ghz-16-core-lga-1700-processor/"
# url = "https://www.primeabgb.com/online-price-reviews-india/colorful-igame-geforce-rtx-3070-ti-ultra-w-oc-8g-v-graphic-card/"


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
       "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
       "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(url, timeout=2, headers=headers)
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
print(price_el)