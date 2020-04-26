from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    breaking_news = get_news('trending')
    print(breaking_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', title = title,general = breaking_news)