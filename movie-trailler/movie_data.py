# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:36:10 2016

@author: edvan.macedo.jr@gmail.com
"""
class MovieData():
     """ This class handle movie's data information """   
    def __init__(self):
        self.get_movie_data()
        
    def get_movie_data(self):
         VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
         return (["2h 34 min", VALID_RATINGS[3], "Crime, Drama","1994",
                   "Pulp Fiction", "The lives of two mob hit men, a boxer,"
                   "a gangster wife, and a pair of diner bandits intertwine in"
                   "four tales of violence and redemption. ",
                   "http://img05.deviantart.net/4591/i/2015/115/7/2/"
                   "pulp_fiction_poster_by_riikardo-d50i7n6.jpg",
                   "https://www.youtube.com/watch?v=s7EdQ4FqbhY"], 
                   ["3h 21min", VALID_RATINGS[2], "Adventure, Drama, Fantasy",
                   "2003", "The Lord of the Rings",
                   "Gandalf and Aragorn lead the World of Men against Sauron's"
                   "army to draw his gaze from Frodo and Sam as they approach"
                   " ount Doom with the One Ring. ",
                   "http://horrornews.net/wp-content/uploads/2016/09/"
                   "LOTR-Return-Of-The-King-poster.jpg",
                   "https://www.youtube.com/watch?v=y2rYRu8UW8M"],
                   ["2h 19min", VALID_RATINGS[3], "Drama", "1999",
                   "Fight Club", "An insomniac office worker, looking for"
                   "a way to change his life, crosses paths with a"
                   "devil-may-care soap maker, forming an underground fight"
                   "club that evolves into something much, much more. ",
                   "http://www.impawards.com/1999/posters/fight_club_ver4.jpg",
                   "https://www.youtube.com/watch?v=SUXWAEX2jlg"],
                   ["2h 4min", VALID_RATINGS[1], "Action, Adventure, Fantasy",
                   "1980", "Star Wars: Episode V - The Empire Strikes Back",
                   "After the rebels have been brutally overpowered by the"
                   "Empire on their newly established base, Luke Skywalker"
                   "takes advanced Jedi training with Master Yoda, while his"
                   "friends are pursued by Darth Vader as part of his plan"
                   "to capture Luke. ",
                   "http://i10.photobucket.com/albums/a116/mikepaul1/"
                   "star-wars-episode-v-the-empire-strikes-back"
                   "-5229c2d4a1c75_zpsmc0wqr6s.jpg",
                   "https://www.youtube.com/watch?v=xESiohGGP7g"],
                   ["2h 22min", VALID_RATINGS[2], "Comedy, Drama", "1994", 
                   "Forrest Gump", "Forrest Gump, while not intelligent, has"
                   "accidentally been present at many historic moments, but"
                   "his true love, Jenny Curran, eludes him. ",
                   "https://s-media-cache-ak0.pinimg.com/736x/cd/d9/e3/"
                   "cdd9e3b6c6072fb0f8c6a54bfc4bc7a4.jpg",
                   "https://www.youtube.com/watch?v=bLvqoHBptjg"],
                   ["2h 28min", VALID_RATINGS[2], "Action, Adventure, Sci-Fi",
                   "2010", "Inception", "A thief, who steals corporate secrets"
                   "through use of dream-sharing technology, is given the"
                   "inverse task of planting an idea into the mind of a CEO.",
                   "https://encrypted-tbn2.gstatic.com/"
                   "images?q=tbn:ANd9GcRMyEwdqYKY8VRxYmWFZxVoJJalccdCZ4ksKC"
                   "iaPH6JYcu2sQhf",
                   "https://www.youtube.com/watch?v=8hP9D6kZseM"])