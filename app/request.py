from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_API_BASE_URL']

...

def get_allnews(category):
    '''
    Function that gets the json response to our url request
    '''
    get_allnews_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_allnews_url) as url:
        get_allnews_data = url.read()
        get_allnews_response = json.loads(get_allnews_data)

        allnews_results = None

        if get_allnews_response['results']:
            allnews_results_list = get_allnews_response['results']
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
        source = news_item.get('source')
        title = news_item.get('title')
        description = news_item.get('description')
        content = news_item.get('content')
        url = news_item.get('url')

        news_object = News(source,title,description,content,url)
        news_results.append(news_object)
       
    return news_results

def get_news(url):
    get_news_details_url = base_url.format(url,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            source = news_details_response.get('source')
            title = news_details_response.get('title')
            description = news_details_response.get('description')
            content = news_details_response.get('content')
            url = news_details_response.get('url')
            
            news_object = News(source,title,description,content,url)

    return news_object