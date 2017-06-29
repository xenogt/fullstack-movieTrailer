import fresh_tomatoes
import media

toy_story = media.Movie(
    'Toy Story',
    'http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
    'https://www.youtube.com/watch?v=vwyZH85NQC4')

movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)