import random
from faker import Faker
fake = Faker()

genre = ['Action', 'Romanse', 'Sport', 'Horror', 'Thriller', 'Adventure', 'Documentary']

class Library:
    def __init__(self, title, release_date, genre, views, type):
        self.title = title
        self.release_date = release_date
        self.genre = genre
        self.views = views
        self.type = type

    def play(self, views):
        views += 1

class Movies(Library):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
    def __repr__(self):
        return f'movie("{self.title}", "{self.genre}", "{self.release_date}", "{self.views}")'
    def __str__(self):
        return f'{self.title} ({self.release_date})'

class Series(Library):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
    def __repr__(self):
        return f'series("{self.title}", "{self.season}", "{self.episode}", "{self.genre}", "{self.release_date}", "{self.views}")'
    def __str__(self):
        if self.episode >= 0 and self.episode < 10:
            if self.season >= 0 and self.season < 10:
                return f'{self.title} S0{self.season}E0{self.episode}'
            else:
                return f'{self.title} S{self.season}E0{self.episode}'
        else:
            if self.season >= 0 and self.season < 10:
                return f'{self.title} S0{self.season}E{self.episode}'
            else:
                return f'{self.title} S{self.season}E{self.episode}'



def List_of_movies_and_series(number):
    empty = []
    for i in range(0, number):
        a = random.randrange(0, 2)
        if a == 0:
            type = 'movie'
        else:
            type = 'series'       
        if type == 'movie':
            a = random.randrange(0, 7)
            titles = fake.word()
            release_dates = fake.date()
            genres = genre[a]
            viewss = fake.pyint()
            types = "movie"
            i = Movies(title=titles, release_date=release_dates, genre=genres, views=viewss, type=types)
            empty.append(i)
        elif type == 'series':
            a = random.randrange(0, 7)
            b = random.randrange(0, 100)
            c = random.randrange(0, 100)
            titles = fake.word()
            release_dates = fake.date()
            genres = genre[a]
            viewss = fake.pyint()
            episodes = b
            seasons = c
            types = "series"
            i = Series(title=titles, release_date=release_dates, genre=genres, views=viewss, episode=episodes, season=seasons, type=types)
            empty.append(i)
    for j in empty:
        print(j)

def get_movies(m):
    movie = []
    for i in m:
        if i.type=="movie":
            movie.append(i)
    print(movie)
                        

a = List_of_movies_and_series(5)
get_movies

#sim = Series(title="The Simpsons", release_date=1999, genre="action", views=55 ,season=10, episode=5)
#pulp = Movies(title="Pulp Fiction", release_date=1994, genre="Romantic", views=90)
