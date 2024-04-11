import argparse

from flask import Flask
from datetime import datetime
# import sys

# weekdays = [('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'),
#             ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
#             {1: 'Понедельник',
#              2: 'Вторник',
#              3: 'Среда',
#              4: 'Четверг',
#              5: 'Пятница',
#              6: 'Суббота',
#              7: 'Воскресенье'}]
# for type_ in weekdays:
#     print(f'For type: {type(type_)}, size is {sys.getsizeof(type_)}')

weekdays = ('Хорошего понедельника', 'Хорошего вторника', 'Хорошей среды', 'Хорошего четверга',
            'Хорошей пятницы', 'Хорошей субботы', 'Хорошего воскресенья')

app = Flask(__name__)


@app.route('/hello-world/<name>')
def get_correct_username_with_weekdate(name):
    weekday = datetime.today().weekday()
    return f'Hello, {name}. {weekdays[weekday]}!'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Запуск Flask приложения')
    parser.add_argument('--port', type=int, default=5000, help='Порт для запуска Flask приложения')
    args = parser.parse_args()

    app.run(debug=True, port=args.port)
