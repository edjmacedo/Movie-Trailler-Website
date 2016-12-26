class VideoInfo():

    """ This class provides a way to store comum information about video
    Attributes:
        duration (str): This should inform the media duration
        ratings (str): This should inform the valid ratings of media
        genre (str): This should inform the genre of media
        date(str): This should inform the date of release of media
    """
    
    VALID_RATINGS = ["G",  "PG",  "PG-13",  "R"] #predefined ratings

    def __init__(self, duration, ratings, genre, date):        
        self.duration = duration
        self.ratings = ratings
        self.genre = genre
        self.date = date