# Example
# Same idea for XML parser - need to set "xml.parser" instead of "html.parser"

from requests import get
from bs4 import BeautifulSoup
from bs4.element import ResultSet

response = get("https://odessa.ithillel.ua/courses/qa-automation-python")

soup = BeautifulSoup(response.content, "html.parser")

blocks: ResultSet = soup.findAll("div", class_="programme-collapsible_body")
headers: ResultSet = soup.findAll("div", class_="programme-collapsible_header")

themes = {}

for header in headers:
    themes[header.text.strip()] = []

themes_names = list(themes.keys())


counter = 0

for block in blocks:
    for item in block:
        themes[themes_names[counter]].append(item.text)
    counter += 1

for key, value in themes.items():
    print(f"{key}: {value}")
