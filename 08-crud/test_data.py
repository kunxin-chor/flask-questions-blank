import data
import pytest
import csv

from shutil import copyfile

def setup_function():
    copyfile('books.csv', 'test_books.csv')
    data.filename = 'test_books.csv'

def teardown_function():
    pass

# to write a test function, the name of the function must start with 'test_'
def test_read_authors_from_file():
    authors = data.read_authors()
    assert len(authors)==1
    assert authors[0]['first_name'] == 'Ronald' # Jinja2: authors.0.first_name, js: authors[0].first_name
    assert authors[0]['last_name'] == 'Tolkien'
    assert authors[0]['date_of_birth'] == '03/01/1892'
    assert authors[0]['gender'] == 'Male'

def test_read_books_from_file():
    library = data.read_books()
    assert len(library)==5
    assert library[0]['title']=='The Lord of the Rings'
    assert library[2]['title']=='Children of Dune'
    assert library[-1]['title']=='Charlie and the Chocolate Factory'

def test_can_list_book():
    books = data.list_book()
    assert len(books)==5

def test_can_find_book():
    book = data.find_book('Twilight')
    print(book)
    assert book != None
    assert book['title'] == 'Twilight'
    assert book['isbn'] == '9780316038379'

def test_add_book():
    data.add_book("11223344", "Ender's Game", "Orson Scott", "15/01/1985")
    book = data.find_book("Ender's Game")
    assert book != None
    assert book['title'] == "Ender's Game"
    assert book['isbn'] =='11223344'
    assert book['author'] == 'Orson Scott'
    assert book['year_published'] == "15/01/1985"

def test_modify_book():
    library = data.modify_book('9780316038379', 'Twilight 2', 'Meyer Stephenie 2','1/1/2020')
    assert library[3]['title'] == 'Twilight 2'
    assert library[3]['author'] == 'Meyer Stephenie 2'
    assert library[3]['year_published'] == '1/1/2020'

def test_save_book():
    library = data.modify_book('9780316038379', 'Twilight 2', 'Meyer Stephenie 2','1/1/2020')
    data.save(library) # save to file
    books = data.read_books()
    assert books[3]['title'] == 'Twilight 2'
    assert books[3]['author'] == 'Meyer Stephenie 2'
    assert books[3]['year_published'] == '1/1/2020'


