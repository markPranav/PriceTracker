import re
from bs4 import BeautifulSoup
import requests

# url = "https://mdcomputers.in/asus-rog-strix-rtx3070ti-o8g-gaming.html"
# url = "https://www.vishalperipherals.in/colorful-igame-geforce-rtx3070ti-ultra-w-oc-8g-v?manufacturer_id=94"
url = "https://www.easyshoppi.com/product/igame-geforce-rtx-3070-ti-ultra-w-oc-8g-v/"
# url = "https://www.primeabgb.com/online-price-reviews-india/colorful-igame-geforce-rtx-3070-ti-ultra-w-oc-8g-v-graphic-card/"


page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

if(soup.find(class_=re.compile("woocommerce"))):
    price_el = soup.find('p',class_=re.compile("price")).getText().split()
    stock = soup.find(class_=re.compile("stock-availability")).get_text().lower()
    stock = "in stock" in stock
else:
    price_el = [soup.find(class_=re.compile("price-new")).getText().strip(), soup.find(class_=re.compile("price-old")).getText().strip()]
    stock = soup.find(class_=re.compile("stock")).get_text().lower()
    stock = "in stock" in stock

price_el = list(map(lambda x: float(re.sub(r'[^\d.]', '', x)), price_el))
price_el.sort()
price_el.append(stock)
print(price_el)