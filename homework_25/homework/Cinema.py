from homework_25.homework.movie_adapter import MovieAdapter


class Cinema:

    @staticmethod
    def showcase():
        tmp = MovieAdapter.get_movies()
        for show in tmp:
            print(show)


t = Cinema()
t.showcase()