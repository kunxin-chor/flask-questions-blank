from flask import Flask, render_template, request, redirect, url_for
import data
import os

app = Flask(__name__)

@app.route('/')
def index():
    library = data.read_books()
    return render_template('index.template.html',library=library)

@app.route('/search')
def search():
    return render_template('search.template.html')

@app.route('/search', methods=["POST"])
def process_search():
    title_wanted = request.form.get('search_terms')
    book = data.find_book(title_wanted)
    return render_template('display_search_result.template.html', book=book)
    
@app.route('/add')
def add():
    return render_template("add.template.html")

@app.route('/add', methods=['POST'])
def process_add_book():
    isbn = request.form.get('isbn')
    title = request.form.get('title')
    author = request.form.get('author')
    year_published = request.form.get('year_published')
    data.add_book(isbn, title, author, year_published)
    return redirect(url_for('index'))

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)