class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,title,overview,poster,source):
        self.id =id
        self.title = title
        self.overview = overview
        self.poster = 'https://image.tmdb.org/t/p/w500/'+ poster
        self.source = source