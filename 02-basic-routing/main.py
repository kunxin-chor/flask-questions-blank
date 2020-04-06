from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# your code here

# Routes are URL paired to a python function
# and the functions are also known as the 'view' functions

# @ is as an annotation
@app.route('/')
def hello():
    return "hi everybody"

@app.route('/about')
def about():
    return "i am very smart"

# we can pass in route parameters
# a route parameter is an argument, but this time round is passed via the URL
# the <number> is an argument which we are going to pass to the view function
@app.route('/double/<number>')
def double(number):
    return str(int(number) * 2)

@app.route('/add_two/<n1>/<n2>')
def add_two(n1, n2):
    return str(int(n1)+int(n2))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)