import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.daft.ie/property-for-rent/ireland/houses?location=cork-commuter-towns-cork&location=cork-city').text
soup = BeautifulSoup(r, 'html.parser')
data = soup.find_all("div", class_="Card__Body-x1sjdn-3 dhiEPC")
links = soup.find('a')

for datas in data:
    price = datas.find("div", class_="TitleBlock__Price-sc-1avkvav-3 pJtsY").text
    address = datas.find("p", class_="TitleBlock__Address-sc-1avkvav-7 knPImU").text
    URL = datas.find_all('a')
    print(f"Address:{address} Price is {price}")
    print("test link:", URL)
