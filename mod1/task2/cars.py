from flask import Flask

app = Flask(__name__)
car_list = ['Chevrolet', 'Renault', 'Ford', 'Lada']

@app.route('/cars')
def cars():
    return ', '.join(car_list)
if __name__ == '__main__':
    app.run(debug=True, port=5555)