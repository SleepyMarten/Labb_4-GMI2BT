from flask import Flask, request, Response, render_template
from weather_modules import db_connect, save_data
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("weather.html")

#request data from the flask server
@app.route("/post_data", methods=['POST'])
def post_data():
    respond = request.get_json()
    db_connect()
    save_data(respond)
    return "Data was added to the database!"

#show datas in weather.db
@app.route("/weather", methods = ['GET'])
def weather():
    conn = db_connect()
    c = conn.cursor()
    c.execute("SELECT * from Weather")
    weather_data = c.fetchall()
    return render_template("weather.html",  data = weather_data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug = True)