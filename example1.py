# Создайте новое приложение Flask, которое будет отображать
# текущие дату и время на главной странице.
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def current_date_time():
    now = datetime.now()
    current_date = now.strftime("%d.%m.%Y")
    current_time = now.strftime("%H:%M:%S")
    return (f"<h3>Сегодня:</h3><p>{current_date}</p>"
            f"<h3>Текущее время:</h3><p>{current_time}</p>")


if __name__ == '__main__':
    app.run(debug=True)
