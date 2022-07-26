from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello Word"

@app.route("/meucontato")
def meucontato():
    return render_template('index.html')
