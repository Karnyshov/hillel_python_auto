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


class Movie:
    def __init__(self, category: str, decade: str, title: str, form: str, year: str, rating: str, description: str):
        self.category = category
        self.decade = decade
        self.title = title
        self.form = form
        self.year = year
        self.rating = rating
        self.description = description
