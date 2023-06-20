"""
Создать адаптер Movie в котором будет инкапсулирована логика преобразования xml в список объектов Movie.
В метод можете передавать либо путь к файлу либо корень документа на ваш выбор.
В объекте должны быть следующие поля:
- category
- decade
- title
- format
- year
- rating
- description
"""
from xml.etree import ElementTree

tree = ElementTree.parse("movies.xml")
root = tree.getroot()

movies_list = []

for genre in root.findall("genre"):
    category = genre.attrib["category"]
    for decades in genre.findall("decade"):
        decade = decades.attrib["years"]
        for movie in decades.findall("movie"):
            tmp = {"category": category,
                   "decade": decade,
                   "title": movie.attrib["title"],
                   "format": movie.find("format").text,
                   "year": movie.find("year").text,
                   "rating": movie.find("rating").text,
                   "description": movie.find("description").text}
            movies_list.append(tmp)

print(movies_list)
