import bs4
from bs4 import BeautifulSoup
import requests


def get_score(brand_name):

    search_url = f"https://directory.goodonyou.eco/brand/{brand_name}"
    markup = requests.get(search_url).text

    soup = BeautifulSoup(markup, 'lxml')

    result = soup.find_all("span", class_="LabelMeter__TextScore-sc-6zrovj-2")

    if result:
        scores = [int(span.get_text().split(" ")[0]) for span in result]
        return {
            'planet': scores[0],
            'people': scores[1],
            'animals': scores[2]
        }
    else:
        return False



