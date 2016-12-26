# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:32:52 2016

@author: edvan.macedo.jr@gmail.com
"""

import video_info

class Movie(video_info.VideoInfo):
    
    """ This class provides the data base for movie
    Attributes:
        duration (str): This should inform the media duration
        ratings (str): This should inform the valid ratings of media
        genre (str): This should inform the genre of media
        date(str): This should inform the date of release of media
        movie_title(str): This should inform the movie title
        movie_storyline(str): This should inform short description of movie
        poster_image(str): This should provide the URL image for movie poster
        trailer_youtube(str): This should provide the URL for movie trailer
    """
    def __init__(self, duration, ratings, genre, date, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        video_info.VideoInfo.__init__(self, duration, ratings, genre, date)        
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube