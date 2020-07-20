from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    # print('Success')
    return render_template('home.html', hello='Sean')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles', methods= ['GET', 'POST'])
def articles():
    print('success')
    articles = Articles()
    print(len(articles))
    return render_template('articles.html', articles = articles)




if __name__=="__main__":
    app.run()