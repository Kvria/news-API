from flask import render_template
from app import app
from .request import get_news


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting breaking news
    general_news = get_news('general')
    sports_news = get_news('sports')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', general = general_news, sports = sports_news )


@app.route('/news/<news_url>')
def movie(news_url):

    '''
    View movie page function that returns the news details page and its data
    '''
    title = f'You are viewing {news_url}'
    return render_template('news.html',title = title)