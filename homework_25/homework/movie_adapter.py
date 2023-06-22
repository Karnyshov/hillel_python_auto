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
from homework_25.homework.xml_parser import XMLParser


class MovieAdapter:

    def __init__(self, xml_parser: XMLParser):
        self.xml_parser = xml_parser
        self.movies = []

    def get_movies(self):
        self.movies = self.xml_parser.parse_movies()
