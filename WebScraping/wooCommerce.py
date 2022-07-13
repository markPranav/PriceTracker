import re
from bs4 import BeautifulSoup
import requests

url = "https://www.easyshoppi.com/product/igame-geforce-rtx-3070-ti-ultra-w-oc-8g-v/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

price_el = soup.find('p', class_="price")
# print(price_el)
print(price_el.get_text().split())