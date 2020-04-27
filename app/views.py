from flask import render_template
from app import app
from .request import get_allnews,get_news,search_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting breaking news
    general_news = get_news('general')
    sports_news = get_news('sports')

    title = 'Home - Welcome to The best News Review Website Online'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', general = general_news, sports = sports_news )


@app.route('/news/<news_url>')
def news(news_url):

    '''
    View news page function that returns the news details page and its data
    '''
    
    movie = get_news(url)
    title = f'{news.title}'

    return render_template('news.html',title = title)

@app.route('/search/<news_name>')
def search(news_name):
    '''
    View function to display the search results
    '''
    news_name_list = news_name.split(" ")
    news_name_format = "+".join(news_name_list)
    searched_news = search_news(news_name_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)