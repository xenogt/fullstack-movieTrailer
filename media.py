import webbrowser

class Movie():
    '''Blueprint for creating movie objects'''
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    '''method to play the movie's trailer'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
