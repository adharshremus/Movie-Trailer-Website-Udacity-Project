import webbrowser
class Movie():
    """ 'self' keyword we can access the attributes and methods of the class in python for __init__
    Arguments:
    parameter 1: address the movie_title 
    parameter 2: pops up the storyline with respective movie
    parameter 3: shows poster of the movie
    parameter 4: URL for trailer of the movie """
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
      
    def show_trailer(self):
        
        webbrowser.open(self.trailer_youtube_url)

