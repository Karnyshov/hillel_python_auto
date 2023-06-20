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
movie_fields = {}

# TODO: fix list appending and duplicate
for genre in root.findall("genre"):
    movie_fields["category"] = genre.attrib["category"]
    for decade in genre.findall("decade"):
        movie_fields["decade"] = decade.attrib["years"]
        for movie in decade.findall("movie"):
            movie_fields["title"] = movie.attrib["title"]
            movie_fields["format"] = movie.find("format").text
            movie_fields["year"] = movie.find("year").text
            movie_fields["rating"] = movie.find("rating").text
            movie_fields["description"] = movie.find("description").text
            print(movie_fields)
            movies_list.append(movie_fields)
            print(movies_list)
