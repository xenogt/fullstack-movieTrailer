import fresh_tomatoes
import media

#each movie objects below has 3 fields, title, poster_image_url and trailer_youtube_url
transformer = media.Movie(
    'Transformer',
    'https://image.tmdb.org/t/p/w640/f8Ng1Sgb3VLiSwAvrfKeQPzvlfr.jpg',
    'https://www.youtube.com/watch?v=6Vtf0MszgP8')

beauty_and_beast = media.Movie(
    'Beauty And The Beast',
    'https://image.tmdb.org/t/p/w640/tWqifoYuwLETmmasnGHO7xBjEtt.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY')

despicable_me = media.Movie(
    'Despicable Me 3',
    'https://image.tmdb.org/t/p/w640/5qcUGqWoWhEsoQwNUrtf3y3fcWn.jpg',
    'https://www.youtube.com/watch?v=euz-KBBfAAo')

lord_of_ring = media.Movie(
    'Lord of the Rings',
    'https://image.tmdb.org/t/p/w640/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
    'https://www.youtube.com/watch?v=V75dMMIW2B4')

harry_potter = media.Movie(
    'Harry Potter',
    'https://image.tmdb.org/t/p/w640/dCtFvscYcXQKTNvyyaQr2g2UacJ.jpg',
    'https://www.youtube.com/watch?v=dtiklALGz20')

hunger_games = media.Movie(
    'Hunger Games',
    'http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
    'https://www.youtube.com/watch?v=PbA63a7H0bo')

wonder_woman = media.Movie(
    'Wonder Woman',
    'https://image.tmdb.org/t/p/w640/gfJGlDaHuWimErCr5Ql0I8x9QSy.jpg',
    'https://www.youtube.com/watch?v=INLzqh7rZ-U')

warcraft = media.Movie(
    'Warcraft',
    'https://image.tmdb.org/t/p/w640/ckrTPz6FZ35L5ybjqvkLWzzSLO7.jpg',
    'https://www.youtube.com/watch?v=RhFMIRuHAL4')
    
the_foreigner = media.Movie(
    'The Foreigner',
    'https://image.tmdb.org/t/p/w640/mZ6G8LorvBJ9LdzE2XhePLUtWpy.jpg',
    'https://www.youtube.com/watch?v=LmImJ6ZUiqE')

#list of movie instances created from media.Movie class
movies = [transformer, beauty_and_beast, despicable_me, hunger_games, lord_of_ring, harry_potter, wonder_woman, warcraft, the_foreigner]

#calling the open_movies_page method in fresh_tomatoes file, passed in the movies array as argument.
fresh_tomatoes.open_movies_page(movies)