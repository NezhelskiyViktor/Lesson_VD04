# Создайте новое приложение Flask, создайте структуру проекта
# с папками static и templates, в папке templates должны быть
# 3 html файла: index, blog, contacts (главная страница,
# страница блога и контакты). Заполните их информацией и
# выведите силами flask сервера, используя функцию
# render_template()
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run(debug=True)
