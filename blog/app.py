from flask import Flask, render_template, redirect, flash
from article_data import Articles
from forms import LoginForms
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

Articles = Articles()

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/articles/<string:id>/')
def display_article(id):
    return render_template('article.html', id=id)


# Route for handling the login page logic
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)