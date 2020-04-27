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
    sports_news = get_movies('sports')
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', general = general, sports = sports )