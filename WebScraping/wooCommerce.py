from bs4 import BeautifulSoup
import requests

url = "https://www.pcstudio.in/product/msi-rtx-3080-ventus-3x-plus-oc-lhr-10gb-graphics-card/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

price_el = soup.find('p', class_='price')

print(price_el.get_text().split())