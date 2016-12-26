# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:32:52 2016

@author: edvan.macedo.jr@gmail.com
"""

import videoinfo

class Media(videoinfo.VideoInfo):

    def __init__(self, duration, ratings, genre, date, movie_title, movie_storyline, poster_image, trailer_youtube):
        videoinfo.VideoInfo.__init__(self, duration, ratings, genre, date)        
        self.movie_title = movie_title
        self.movie_storyline = movie_storyline
        self.poster_image = poster_image
        self.trailer_youtube = trailer_youtube

moviemedia = Media("1 hora", videoinfo.VideoInfo.VALID_RATINGS[2], "comedy", "1998", "filme teste", "filme descricao", "url image", "url trailler")

print(moviemedia.ratings)
