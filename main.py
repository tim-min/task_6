from flask import Flask, url_for, request
import os

app = Flask(__name__)


@app.route('/')
def name():
    return "<h style='font-weight: bold'>Миссия Колонизация Марса<h>"


@app.route('/index')
def div():
    return "<h style='font-weight: bold'>И на Марсе будут яблони цвести!<h>"


@app.route('/promotion')
def promotion():
    return """<strong>Человечество вырастает из детства.</strong> <br>
            <strong>Человечеству мала одна планета.</strong> <br>
            <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
            <strong>И начнем с Марса!</strong>
            <strong>Присоединяйся!</strong>"""

@app.route('/image_mars')
def image_page():
    return f"""<html>
                <head>
                <title>Привет, Марс!</title>
                </head>
                <body>
                <h1>Жди нас, Марс!</h1><br>
                <img src={url_for('static', filename="images/mars.jpg")} width=800px height=500px></img><br>
                <h4>Вот она какая, красная планета</h4>
                </body>
                </html>"""

@app.route("/promotion_image")
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="style.css" crossorigin="anonymous">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src={url_for('static', filename="images/mars.jpg")} width=300px height=200px></img><br><br>
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <div align="center">
                            <h4>Анкета претендента</h1>
                            <h5>на участие в миссии</h2>
                            </div>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="input" class="form-control" id="user_surname" placeholder="Введите фамилию" name="surname">
                                    <input type="input" class="form-control" id="user_name" placeholder="Введите имя" name="name"><br>
                                    <input type="email" class="form-control" aria-describedby="emailHelp" id="user_email" placeholder="Введите ваш email" name="email">
                                    <br><div class="form-group">
                                        <label for="eduSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="eduSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <br>
                                     <div class="form-group">
                                        <label for="form-check">Какие у Вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_0" value="prof_0" checked>
                                          <label class="form-check-label" for="prof_0">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_1" value="prof_1">
                                          <label class="form-check-label" for="prof_1">
                                            Инженер-строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_2" value="prof_2">
                                          <label class="form-check-label" for="prof_2">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_3" value="prof_3">
                                          <label class="form-check-label" for="prof_3">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_4" value="prof_4">
                                          <label class="form-check-label" for="prof_4">
                                            Инженер по жизнеобеспечению
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_5" value="prof_5">
                                          <label class="form-check-label" for="prof_5">
                                            Инженер по радиационной защите
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_6" value="prof_6">
                                          <label class="form-check-label" for="prof_6">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="prof" id="prof_7" value="prof_7">
                                          <label class="form-check-label" for="prof_7">
                                            Оператор марсохода
                                          </label>
                                        </div>
                                    </div>
                                    <br>

                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <br>

                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
                                    </div><br>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы ли вы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                                <br><br>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['user_surname'])
        print(request.form['user_name'])
        print(request.form['user_email'])
        print(request.form['education'])
        print(request.form['reason'])
        print(request.form['prof'])
        return "Форма отправлена"

@app.route("/choice/<planet_name>")
def planet_choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="style.css" crossorigin="anonymous">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}</h1>
                    <h3>Эта планета близка к земле;</h3>
                    <div class="alert alert-success" role="alert">
                      <h3>На ней много необходимых ресурсов;</h3>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h3>На ней есть вода и атмосфера;</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h3>На ней есть небольшое магнитное поле;</h3>
                    </div>
                    <div class="alert alert-dark" role="alert">
                      <h3>Наконец, она красива!</h3>
                    </div>
                  </body>
                </html>'''

@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="style.css" crossorigin="anonymous">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h2>Результаты отбора</h1>
                    <h3>Претендента на участие в миссии {nickname}:</h3>
                    <div class="alert alert-success" role="alert">
                      <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    </div>
                    <div class="alert alert-primary" role="alert">
                      <h3>Составляет {rating}!</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h3>Желаем удачи!</h3>
                    </div>
                  </body>
                </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    image = ''
    current_dir = os.path.abspath(__file__).replace("\\", "/").split("/")[-2]
    if os.path.exists(f"{current_dir}/static/images/uploaded_file.jpg"):
        image = f"<br><img src={url_for('static', filename='images/uploaded_file.jpg')}></img><br>"
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                          <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    {image}
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        file = request.files['file']
        current_dir = os.path.abspath(__file__).replace("\\", "/").split("/")[-2]
        file.save(f"{current_dir}/static/images/uploaded_file.jpg")
        file.close()
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                          <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div><br>
                                    <img src={url_for('static', filename='images/uploaded_file.jpg')}></img><br>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route("/carousel")
def mars_pictures():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="style.css" crossorigin="anonymous">

                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>
                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                    <script src="{url_for('static', filename='js/carousel.js')}"></script>
                    <title>Колонизация</title>
                  </head>
                  <body>
                  <div align="center">
                    <h2>Пейзажи Марса</h2>
                  </div>
                  <br>
                  <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
                    <div class="carousel-inner">
                        <div class="carousel-item">
                        <img class="d-block w-100" src="{url_for('static', filename='images/mars_image_1.jpg')}" alt="First slide">
                        </div>
                        <div class="carousel-item active">
                        <img class="d-block w-100" src="{url_for('static', filename='images/mars_image_2.jpg')}" alt="Second slide">
                        </div>
                        <div class="carousel-item">
                        <img class="d-block w-100" src="{url_for('static', filename='images/mars_image_3.jpg')}" alt="Third slide">
                        </div>
                    </div>
                    <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                    </a>
                    <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                    </a>
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
