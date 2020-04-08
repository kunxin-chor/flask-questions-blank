
#DAL -- data access layer
#DAO -- data access object
import csv

# as this is a variable defined outside of any functions
# it is available to all functions.
# i.e, this in the 'global scope' (sometimes known as the 'global frame')
filename = "books.csv"

# the second argument for open_csv i.e process_file, is a function
# the function must take in one argument, and that argument must be a csv reader
def open_csv(f, process_file,newline="\n"):
    result = None; #result has a default of none
    try:
        with open(f, 'r') as fp:
            # create the csv reader
            reader = csv.reader(fp, delimiter=",")    
            # call the process_file function and pass reader to it as the first argument
            result = process_file(reader)
        return result
    except FileNotFoundError:
        return []

# read_books_from_file takes in one argument which has to be a csv reader
def read_books_from_file(reader):
    books = []
    next(reader) #skip the first line
    for l in reader:
        b = {
            'isbn':l[0],
            'title':l[1],
            'author':l[2],
            'year_published':l[3]
        }
        books.append(b)
    return books

def read_authors_from_file(reader):
    authors=[]
    next(reader)
    for l in reader:
        a = {
            'first_name':l[0],
            'last_name':l[1],
            'gender':l[2],
            'date_of_birth':l[3]
        }
        authors.append(a)
    return authors

def read_books():
    return open_csv(filename, read_books_from_file)

def read_authors():
    return open_csv('authors.csv', read_authors_from_file)

def list_book():
    books = read_books()
    final = []
    for b in books:
        final.append(b)
    return final

def find_book(title):
    library = read_books()
    for book in library:
        if book['title'] == title:
            return book

# book is supposed to be a dictionary of key-value pairs
def add_book(isbn, title,author,year_published):
    with open(filename, 'a', newline="\n") as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow([isbn,title,author,year_published])

def modify_book(isbn, title, author, year_published):
    library = read_books()
    for book in library:
        if book['isbn'] == isbn:
            book['author'] = author
            book['title'] = title
            book['year_published'] = year_published
            break
    return library

def save(library):
    print(library)
    with open(filename, 'w', newline='\n') as fp:
        writer = csv.writer(fp, delimiter=",")
        writer.writerow(['isbn', 'title','author','year_published'])
        for b in library:
            isbn =b['isbn']
            title =b['title']
            author=b['author']
            year_published=b['year_published']
            writer.writerow([isbn,title,author,year_published])
        
