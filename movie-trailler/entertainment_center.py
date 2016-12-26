# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:59:39 2016

@author: edvan.macedo.jr@gmail.com
"""

import media
import fresh_tomatoes
import movie_data

class Entertainment():
    
    """ This class create instances of movies and send the list movies """   
          
    def __init__(self):
        # Get all movie data when create an instance of Entertainment class
        self.get_list_movie()
        
    def get_list_movie(self):
        # Return list of movie data
        list_movie = movie_data.MovieData()
        return list_movie.get_movie_data()
                    
    def create_movie_instance(self, media_data):
        # Create instance of each movie
        for i in range(0, len(media_data)):            
            if i == 0:
                duration = media_data[i]
            elif i == 1:
                ratings = media_data[i]
            elif i == 2:
                genre = media_data[i]
            elif i == 3:
                date = media_data[i]
            elif i == 4:
                movie_title = media_data[i]
            elif i == 5:
                movie_storyline = media_data[i]
            elif i == 6:
                poster_image = media_data[i]
            elif i == 7:
                trailer_youtube = media_data[i]
        # Return new instance
        return media.Movie(duration, ratings, genre, date, movie_title,
                    movie_storyline, poster_image, trailer_youtube)
        

# Create new instance of Entertainment class
movies_data = Entertainment()
# Get the list of movies
list_of_movies = movies_data.get_list_movie()
# Initialize control variable          
movie_list = 0
# Initialize empty list to insert instances of media.Movie
movies = []
# Running the list of movies, get the instance was created and insert in 
# list of movies
while len(list_of_movies) > movie_list:
    new_movie = movies_data.create_movie_instance(list_of_movies[movie_list])    
    movies.insert(movie_list, new_movie)    
    movie_list += 1    
# Sent the list of instances to fresh_tomatoes to create HTML page
fresh_tomatoes.open_movies_page(movies)