from homework_25.homework.movie_adapter import MovieAdapter


class Cinema:
    showcase = MovieAdapter.get_movies()


t = Cinema().showcase
print(t)
