from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


name = "Mansur"


@app.route("/about_through_the_link")
def about_through_the_link(name1=name):
    name1 = name1
    return render_template('about_through_the_link.html', name=name1)

@app.route("/about_directly")
def about_directly():
    return f"<h1>Hello, {name}</h1>"

# if __name__ == "__main__":
# 	hello_world()
