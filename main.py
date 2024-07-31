import random as r
import jinja2

from flask import Flask, send_file, url_for, request, render_template

app = Flask(__name__)

list1 = ["Сьогодні вас ", "через тиждень вас", "на цьому тижні вас", "цього місяця вас"]
list2 = ["чекає", "здивує", "зустріне", "привітає"]
list3 = ["гарна звістка", "погана звістка", "радісна новина", "щось добре", "невдача"]


@app.route('/horoscope')
def horoscope():
    response = f"Ваше передбачання: {r.choice(list1)} {r.choice(list2)} {r.choice(list3)}"
    return  response

@app.route('/login/', methods = ['POST', 'GET'])
def send_login():
    if request.method == 'POST':
        user = request.form["name"]
        password = request.form["password"]
        return f"GET-{user}, {password}"
    else:
        return send_file("auth.html")

@app.route('/url_for_test/')
def gfgd():
    return url_for("send_login")

if __name__ == '__main__':
    app.run()
