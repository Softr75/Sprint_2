class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"
    
class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"

comedy_list = Comedy()
drama_list = Drama()

print(comedy_list.add_movie("Большой Куш"))
print(drama_list.add_movie("Оружейный барон"))