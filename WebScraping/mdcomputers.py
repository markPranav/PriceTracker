from bs4 import BeautifulSoup
import requests

url = "https://mdcomputers.in/teamgroup-t-force-delta-rgb-16gb-ddr4-3200mhz-white-tf4d416g3200hc16c01.html"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
price_el = soup.find('span', class_="price-new")

print(price_el.get_text().split())