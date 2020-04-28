from flask import render_template
from . import main
from ..request import get_allnews,get_article


@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting breaking news
    general_news = get_allnews('general')
    sports_news = get_allnews('sports')

    title = 'Home - Welcome to The best News Review Website Online'

    return render_template('index.html', general = general_news, sports = sports_news )


@main.route('/news/<id>')
def article(id):

    '''
    View articles page function that returns the article details page and its data
    '''
    
    articles = get_article(id)

    return render_template('news.html',articles = articles)

