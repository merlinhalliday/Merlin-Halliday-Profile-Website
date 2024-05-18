from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/cv')
def cv_page():
    return render_template("cv.html")


@app.route('/projects')
def projects_page():
    return render_template("projects.html")


app.run(host='0.0.0.0', port=81)
