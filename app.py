#!/usr/bin/env python

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/say-hello')
def say_hello():
    return render_template('say-hello.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=8080)