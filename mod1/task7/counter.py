from flask import Flask


app = Flask(__name__)

visit_counter = 0

@app.route('/counter')
def counter():
    global visit_counter
    visit_counter += 1
    return f'{visit_counter}'

if __name__ == '__main__':
    app.run(debug=True, port=5555)