import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('BBC news','The corona pandemic','This disease it taking over the whole world','Testing remains a key problem across the US but some states have started to lift restrictions.','"http://www.bbc.co.uk/news/world-us-canada-52428994",')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()