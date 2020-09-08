#!/usr/bin/env python
"""" A demo flask app to test some CICD in openshift. To run, install
flask (pip install flask) and run 'flask run' from the same dir as
this module."""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """ Return the home template when given the '/' route """
    return render_template('home.html')


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    """ Return the hello template when given the '/hello/' route """
    return render_template('hello.html', name=name)


@app.route('/about/')
def about():
    """ Return the about template when given the '/about/' route """
    return render_template('about.html')


@app.route('/say-hello')
def say_hello():
    """ Return the say-hello template when given the '/say-hello/' route """
    return render_template('say-hello.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

