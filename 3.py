from flask import Flask, send_file, url_for, request, render_template, redirect, abort

app = Flask(__name__)

test_name = "Python Challenge"
max_score = 100
students = [
{"name": "Vlad", "score": 100},
{"name": "Denis", "score": 99},
{"name": "Kostya", "score": 100},
{"name": "Ivan", "score": 79},
{"name": "Alex", "score": 100}
]

@app.route("/results/")
def results():
    context = {
    "title": "Results",
    "students": students,
    "test_name": test_name,
    "max_score": max_score
    }
    #print(context)
    return render_template("results.html", **context)


@app.route("/")
def index():
    return render_template("base.html", title="Flask")

@app.route("/example/")
def example():
    return  render_template("example.html")
     



app.run(port=34001, debug=True)