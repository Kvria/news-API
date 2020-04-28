class News:
    '''
    News class to define news Objects
    '''

    def __init__(self,id,name,description,url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url

class Article :
    def __init__(self,author,title,content,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.content = content
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt