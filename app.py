from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello Word"

@app.route("/meucontato")
def meucontato():
    return """<html>
    <head>
        <title> titulo </title>
    </head>
    <body>
    <a href="http://oceanbrasil.com"> Isso é um link </a>
    <h1>Luiz Eduardo Matias </h1>
    <h2>testeparaosite@gmail.com </h2>
    <h3>96981189880</h3>
    </body>
    </html>"""
