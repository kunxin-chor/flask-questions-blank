from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    # since are all templates must be in templates folder, there is no need for us
    # to put the ./templates in front. Flask will know that we are supposed to
    # get the templates from the ./templates folder
    #return render_template('./templates/index.template.html') --> this is wrong
    return render_template('index.template.html', message='goodbye cruel world')

@app.route('/gallery')
def show_gallery():
    return render_template('gallery.template.html')

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)