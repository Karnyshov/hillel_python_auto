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


class XMLParser:
    movies_list = []
    tree = ElementTree.parse("movies.xml")
    root = tree.getroot()

    @classmethod
    def parse_movies(cls):
        movies = []
        for genre in cls.root.findall("genre"):
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
                    movies.append(tmp)
        return movies


movies_list = XMLParser.parse_movies()
print(movies_list)

