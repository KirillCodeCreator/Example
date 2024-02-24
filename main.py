from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return ("Человечество вырастает из детства.<br>Человечеству мала одна планета."
            "<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!")


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс!</title><br><h1>Жди нас, Марс!</h1><br><img src="{url_for('static', filename='img/MARS_IMG.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/promotion_image')
def bootstrap():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 style="color: red">Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}">
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!.
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!.
                    </div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_astronaut_selection():
    if request.method == 'GET':
        return f"""<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
            crossorigin="anonymous">
    <link href="{url_for('static', filename='css/style.css')}" rel="stylesheet" type="text/css">
    <title>Отбор астронавтов</title>
</head>
<body>
<h1 align="center">Анкета претендента</h1>
<h2 align="center">на участие в миссии</h2>
<div class="container">
    <form class="login_form" method="post">
        <div class="form-group">
            <input type="text" class="form-control" id="surname" placeholder="Введите фамилию"
                   name="surname" required>
            <input type="text" class="form-control" id="name" placeholder="Введите имя" name="name" required>
        </div>
        <div class="form-group">
            <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                   placeholder="Введите адрес почты" name="email" required>
        </div>
        <div class="form-group">
            <label for="educationSelect">Какое у Вас образование?</label>
            <select class="form-control" id="educationSelect" name="education">
                <option>Начальное</option>
                <option>Основное</option>
                <option>Среднее</option>
                <option>Высшее</option>
            </select>
        </div>
        <div class="form-group">
            <label for="professions">Какие у Вас есть профессии?</label>
            <div class="form-check" id="professions">
                <input type="checkbox" class="form-check-input" id="engineerExplorer"
                       name="profession" value="Инженер-исследователь">
                <label class="form-check-label" for="engineerExplorer">Инженер-исследователь</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerBuilder"
                       name="profession" value="Инженер-строитель">
                <label class="form-check-label" for="engineerBuilder">Инженер-строитель</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="pilot" name="profession" value="Пилот">
                <label class="form-check-label" for="pilot">Пилот</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="meteorologist" name="profession" value="Метеорологист">
                <label class="form-check-label" for="meteorologist">Метеорологист</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerLifeSupport"
                       name="profession" value="Инженер по жизнеобеспечению">
                <label class="form-check-label" for="engineerLifeSupport">Инженер по
                    жизнеобеспечению</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="engineerRadioactivityProtection"
                       name="profession" value="Инженер по защите от радиоактивности">
                <label class="form-check-label" for="engineerRadioactivityProtection">Инженер по
                    защите от радиоактивности</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="doctor" name="profession" value="Врач">
                <label class="form-check-label" for="doctor">Врач</label>
            </div>
            <div class="form-check">
                <input type="checkbox" class="form-check-input" id="exobiologist" name="profession" value="Экзобиолог">
                <label class="form-check-label" for="exobiologist">Экзобиолог</label>
            </div>
        </div>
        <div class="form-group">
            <label for="sex">Укажите пол</label>
            <div class="form-check" id="sex">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male"
                       checked>
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
        <div class="form-group">
            <label for="reason">Почему Вы хотите принять участие в миссии</label>
            <textarea class="form-control" id="reason" rows="3" name="reason"></textarea>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptStay" name="accept">
            <label class="form-check-label" for="acceptStay">Готовы остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
</div>
</body>
</html>"""
    elif request.method == 'POST':
        print(request.form['name'])
        print(request.form['surname'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form.getlist('profession'))
        print(request.form['profession'])
        print(request.form['reason'])
        print(request.form['accept'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def greeting(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Моё предложение: {planet_name}!</h1>
                    <h2>Эта планета близка к Земле;</h2>
                    <div class="alert alert-success" role="alert">
                      На ней много необходимых ресурсов;
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      На ней есть вода и атмосфера;
                    </div>
                    <div class="alert alert-warning" role="alert">
                      На ней есть небольшое магнитное поле;
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Наконец, она просто красивая!
                    </div>
                  </body>
                </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      Поздравляем Ваш рейтинг после {level} этапа отбора
                    </div>
                    <h3>составляет {rating}!</h3>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                    </div>
                  </body>
                </html>'''


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
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
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        print(f.read())
        return "Форма отправлена"


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
<div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
    <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
  </ol>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="{url_for('static', filename='img/mars.jpg')}" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-111" src="{url_for('static', filename='img/mars.jpg')}" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-112" src="{url_for('static', filename='img/mars.jpg')}" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
