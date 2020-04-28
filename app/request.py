import urllib.request,json
from .model import News,Article


# Getting api key
api_key = None

# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_allnews(category):
    '''
    Function that gets the json response to our url request
    '''
    get_allnews_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_allnews_url) as url:
        get_allnews_data = url.read()
        get_allnews_response = json.loads(get_allnews_data)

        allnews_results = None

        if get_allnews_response['sources']:
            allnews_results_list = get_allnews_response['sources']
            allnews_results = process_results(allnews_results_list)


    return allnews_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')

        news_object = News(id,name,description,url)
        news_results.append(news_object)
       
    return news_results



def get_article(id):
    news_url = 'http://newsapi.org/v2/everything?sources={}&apiKey={}'
    get_article_details_url = news_url.format(id,api_key)

    with urllib.request.urlopen(get_article_details_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        article_results = []
        
        if article_details_response['articles']:
            article_list = article_details_response['articles']
            for article in article_list:
                author = article.get('author')
                title = article.get('title')
                content = article.get('content')
                urlToImage= article.get('urlToImage')
                publishedAt = article.get('publishedAt')

                article_object = Article(author,title,content,urlToImage,publishedAt)
                article_results.append(article_object) 

    return article_results
