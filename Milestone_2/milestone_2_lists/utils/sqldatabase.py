""" Storing and retrieving from a DB"""
import sqlite3
from collections import defaultdict
from json import JSONDecodeError

def connect_to_db():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    return cursor, connection

def create_db():
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('CREATE TABLE books(name text primary key, author text, read integer)')
    sql_connection.commit()
    sql_connection.close()


def add_book(book):
    # get books
    current_books = get_books()
    # write new book
    current_books['books'].append(book)
    success = write_books(current_books)
    if success:
        return f"{book['name']} was added!"
    else:
        return f"{book['name']} was not added!"


def write_books(book_list):
    with open('book_database.txt', 'w') as file:
        json.dump(book_list, file)
    return True


def get_books():
    with open('book_database.txt', 'r') as file:
        try:
            book_list = json.loads(file.read())
        except JSONDecodeError:
            book_list = defaultdict(list)
    return book_list


def find_book(look_book):
    current_books = get_books()
    found_book = False
    for book in current_books['books']:
        if book['name'] == look_book['name'] and book['author'] == look_book['author']:
            found_book = book
    return found_book


def mark_book_as_read(found_book):
    current_books = get_books()
    marked_book = False
    for book in current_books['books']:
        if book['name'] == found_book['name'] and book['author'] == found_book['author']:
            marked_book = book
            marked_book['read'] = True
    write_books(current_books)
    return marked_book


def delete_book(book_to_delete):
    current_books = get_books()
    new_books = []
    for book in current_books['books']:
        if book != book_to_delete:
            new_books.append(book)
    write_books(new_books)
    return book_to_delete