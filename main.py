from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'
app.config['FLATPAGES_ROOT'] = 'content'
flatpages = FlatPages(app)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/about')
def about_page():
    about_articles = flatpages.get_or_404('about')
    return render_template("about.html", articles=about_articles)


@app.route('/cv')
def cv_page():
    return render_template("cv.html")


@app.route('/projects')
def projects_page():
    return render_template("projects.html")

@app.route('/test')
def test_page():
    page = flatpages.get_or_404('test')
    return render_template("page.html", page=page)


app.run(host='0.0.0.0', port=81)
