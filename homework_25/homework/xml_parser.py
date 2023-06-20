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

# TODO: fix list appending and duplicate
for genre in root.findall("genre"):
    # movies_list.append(movie_fields["category"])
    category = {"category": genre.attrib["category"]}
    # print(category)
    # movies_list.append({"category": genre.attrib["category"]})
    for decades in genre.findall("decade"):
        # movies_list.append({"decade": decades.attrib["years"]})
        decade = {"decade": decades.attrib["years"]}
        # print(decade)
        # category.update(decade)
        # print(category)
        for movie in decades.findall("movie"):
            # category.update(decade)
            tmp = {"title": movie.attrib["title"],
                   "format": movie.find("format").text,
                   "year": movie.find("year").text,
                   "rating": movie.find("rating").text,
                   "description": movie.find("description").text}
            # category.update(decade)
            # print(category)
            # category.update(tmp)
            # print(category)
            decade.update(tmp)
            category.update(decade)
            print(category)
            # print(decade)
            # movies_list.append(tmp)
            # print(movies_list)

# print(movies_list)
