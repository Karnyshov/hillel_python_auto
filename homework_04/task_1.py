import requests
import re

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/"
respond_text = ''

respond = requests.get(url)

if respond.ok:
    respond_text = respond.text

text = respond_text
title_lst = [x.start() for x in re.finditer("tile-cats__heading ng-star-inserted", text)]
title_res = []
dictionary = {}

# Task 1
for x in title_lst:
    header_start = x
    header_end = text.find("</a>", x)
    header = text[header_start:header_end]

    header_title_start = header.find("title=\"") + len("title=\"")
    header_title_end = header.find("\">", header_title_start)
    header_title = header[header_title_start:header_title_end]

    title_res.append(header_title)

# Task 2
for x in range(len(title_res)):
    header_start = title_lst[x]
    header_end = text.find("</a>", title_lst[x])
    header = text[header_start:header_end]

    header_url_start = header.find("href=\"") + len("href=\"")
    header_url_end = header.find("\"", header_url_start)
    header_url = header[header_url_start:header_url_end]

    dictionary[title_res[x]] = header_url

# Task 3
lists_lst = [x.start() for x in re.finditer("tile-cats__list ng-star-inserted", text)]
print(lists_lst)

for z in dictionary:
    dictionary[z] = [dictionary[z]]

    for x in lists_lst:
        list_start = x
        list_end = text.find("/ul", list_start)
        whole_list = text[list_start:list_end]

        list_elements_lst = [x.start() for x in re.finditer("tile-cats__item ng-star-inserted", whole_list)]

        for y in range(len(list_elements_lst)):
            list_element_start = list_elements_lst[y]
            list_element_end = whole_list.find("</a>", list_element_start)
            list_element = whole_list[list_element_start:list_element_end]

            list_element_title_start = list_element.find("title=\"") + len("title=\"")
            list_element_title_end = list_element.find("\"", list_element_title_start)
            list_element_title = list_element[list_element_title_start:list_element_title_end]

            dictionary[z].append(list_element_title)

print(dictionary)
