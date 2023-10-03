from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")      #decoratate function http的網址頁 "/"是指根目錄
def index():       
    return render_template ("index.html")

@app.route("/Hello World")          #第二頁網址
def hello_world():
    return "<h1>Hello World!</h1>"