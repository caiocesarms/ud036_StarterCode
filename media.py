import webbrowser


class Video():
    """Essa classe permite armazenar informacoes sobre videos, servindo de base para outras classes relacionadas"""
    # Construtor da classe
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration


class Movie(Video):
    """Essa classe permite armazenar informacoes sobre filmes"""
    # Construtor da classe
    def __init__(self, movie_title, movie_duration, movie_storyline, poster_image, trailer_youtube):
        Video.__init__(self, movie_title, movie_duration)
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Esse metodo abre uma pagina web usandoa url do trailer fornecida pelo objeto do filme
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class TvShow(Video):
    """Essa classe permite armazenar informacoes sobre shows de TV"""
    # Construtor da classe
    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
