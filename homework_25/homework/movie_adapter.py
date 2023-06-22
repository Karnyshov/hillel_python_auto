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
from homework_25.homework.Movie import Movie


class MovieAdapter:
    xml_parser = XMLParser()

    @classmethod
    def get_movies(cls):
        movie_list = []
        parsed_movies = cls.xml_parser.parse_movies()
        for movie in parsed_movies:
            tmp = Movie(movie.get("category"),
                        movie.get("decade"),
                        movie.get("title"),
                        movie.get("format"),
                        movie.get("year"),
                        movie.get("rating"),
                        movie.get("description"))
            movie_list.append(tmp)
        return movie_list
