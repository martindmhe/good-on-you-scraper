from bs4 import BeautifulSoup
import requests

keywords = input("Describe the item you want to replace: ").strip().split(" ")
max_price = float(input("What is your maximum price?: "))

search_query = "+".join(keywords)
search_url = f"https://www.google.com/search?tbm=shop&q={search_query}"
# search_url = f"https://www.bing.com/shop?q={search_query}"

html_file = requests.get(search_url).text
soup = BeautifulSoup(html_file, 'lxml')

data = soup.find_all("div", class_="u30d4")

products = []

for product in data:
    pass


# with open("file2.html", "w") as file:
#     file.write(soup.prettify())



