from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('имя', validators=[DataRequired()])
    password = StringField('номер телефона', validators=[DataRequired()])
    submit = SubmitField('заказать')


@app.route('/')
def index():
    return f"""<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>главная</title>
                </head>
                <body>
                <header>
                    <nav class="navbar navbar-light bg-light">
                        <a class="navbar-brand" href="/">тюльпанчик</a>
                        <a class="navbar-brand" href="/choose">выбрать букет</a>
                        <a class="navbar-brand" href="/order">сделать заказ</a>
                    </nav>
                </header> 
                <div class="image-text-container">
                    <div style="position: relative; text-align:center;">
                      <img src="{url_for('static', filename='img/fon1.jpg')}"
                               alt="здесь должна была быть картинка, но не нашлась">
                    </div>
                      <div style="position: absolute; top: 30%; left: 20%; transform: translate(-50%, -50%);">
                      <div class="title">
                        <p>тюльпанчик</p>
                          <div class="description">
                            <p>поможем сделать идеальный сюрприз<br></br>
                            режим работы: 10:00 - 22:00<br></br>
                            +7(777)-777-77-77<br></br>
                          ул. Петровка 34</p>
                          </div>
                          <a href="/choose" class="btn btn-outline-light" role="button" data-bs-toggle="button">выбрать букет</a>
                      </div>
                      
                    </div>
                </div>
                
                <img src="{url_for('static', filename='img/fon.jpg')}"
                               alt="здесь должна была быть картинка, но не нашлась">
                
                <footer>
                   <div class="container">
                      <p>designed by beketosic</p>
                   </div>
                </footer>
                </main>
                </body>"""


@app.route('/choose', methods=['GET', 'POST'])
def choose():
    return f'''<!doctype html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
          crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>выбрать букет</title>
                </head>
                <body>
                <header>
                    <nav class="navbar navbar-light bg-light">
                        <a class="navbar-brand" href="/">тюльпанчик</a>
                        <a class="navbar-brand" href="/choose">выбрать букет</a>
                        <a class="navbar-brand" href="/order">сделать заказ</a>
                    </nav>
                </header> 
                <div class="wrapper">
                  <div class="image-container">
                      <div class="header">
                              <p>каталог</p>
                      </div>
                    <img class="image-one" src="{url_for('static', filename='img/fon3.jpg')}">
                    <img class="image-two" src="{url_for('static', filename='img/fon4.jpg')}">
                  </div>
                  <div class="box-container">
                    <div class="box">
                      <img src="{url_for('static', filename='img/гипсофила.jpg')}">
                      <p>гипсофила  499р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/тюльпаны.jpg')}">
                      <p>тюльпаны  299р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/розы.jpg')}">
                      <p>розы 499р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/лилии.jpg')}">
                      <p>лилии 399р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/пионы.jpg')}">
                      <p>пионы 399р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/гвоздика.jpg')}">
                      <p>гвоздики 299р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/гербера.jpg')}">
                      <p>гербера 399р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/ромашки.jpg')}">
                      <p>ромашки 299р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                    <div class="box">
                      <img src="{url_for('static', filename='img/мимоза.jpg')}">
                      <p>мимоза 299р</p>
                      <a href="/order" class="btn btn-outline-dark" role="button" data-bs-toggle="button">заказать</a>
                    </div>
                  </div>
                </div>
                <footer>
                   <div class="container">
                      <p>designed by beketosic</p>
                   </div>
                </footer>
                </main>
                </body>
                </html>'''


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('order.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
