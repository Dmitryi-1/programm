from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/get_time/now')
def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Точное время: {current_time}"