from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
import pymysql
from data import Articles

app = Flask(__name__)
app.debug = True

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'myflaskapp'

db = pymysql.connect(host='localhost',
                port=3306,
                user='root',
                passwd='1234',
                db='myflaskapp')

cursor = db.cursor()


@ app.route('/')
def index():

# print('Success')
    return render_template('home.html', hello='Sean')


@ app.route('/about')
def about():


    return render_template('about.html')


@ app.route('/articles', methods=['GET', 'POST'])
def articles():


    print('success')
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles=articles)


@ app.route('/test')
def show_image():


    return render_template('image.html')


@ app.route('/article/<int:id>')
def article(id):


    articles = Articles()[id-1]
    print(articles)
    return render_template('article.html', data=articles)


if __name__ == "__main__":
    app.run()
