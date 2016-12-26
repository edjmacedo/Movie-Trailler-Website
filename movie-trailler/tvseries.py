# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:40:52 2016

@author: edjmacedo
"""
import videoinfo

class TvSeries(videoinfo.VideoInfo):    
    """ This class provides a way to store data from TV-series
    Attributes:
        duration (str): This should inform the media duration
        ratings (str): This should inform the valid ratings of media
        genre (str): This should inform the genre of media
        date(str): This should inform the date of release of media
        episode(str): This should inform the current episode
        seasos(str): This should informe the current season
    """
    def __init__(self, duration, ratings, genre, date, episode, season):
        videoinfo.VideoInfo.__init__(self, duration, ratings, genre, date)
        self.episode = episode
        self.season = season