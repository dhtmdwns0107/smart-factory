### Flask_web

``` python
virtualenv flask_web
cd flask_web
cd Scripts
cd activate
cd ..
>(flask_web) C:\Users\USER\oh\flask_web>
```

app.py 파일을 생성후 다음과 같은 코드 추가



``` python
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/data', method=['POST'])
def index():
    print('Success')
    return render_template('test.html')

if __name__=="__main__":
    app.run()
```



templates 폴더 생성

templates 안에 test.html 파일 생성

그리고 app.py에서 render_templates 임포트 하고 실행하면 된다

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
        <!-- {% block body %} -->
    <h1> TEST {{ hello }} 님</h1>
        <!-- {% endblock %} -->
</body>
</html>
```

navigationbar 

``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    
    <title>Flask_Web</title>
</head>
<body>
    
</body>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
</html>
```

