""" Storing and retrieving from a DB"""
import sqlite3
from typing import List, Dict, Union


Books = List[Dict[str, Union[str, bool]]]


def connect_to_db():
    connection = sqlite3.connect('books.db')
    cursor = connection.cursor()
    return cursor, connection

def create_db() -> None:
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    sql_connection.commit()
    sql_connection.close()


def add_book(book) -> str:
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('INSERT INTO books VALUES(?, ?, ?)',(book["name"],book["author"],book["read"]))
    sql_connection.commit()
    sql_connection.close()
    return f"{book['name']} was added!"

def get_books() -> Books:
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': bool(row[2])} for row in sql_cursor.fetchall()]
    sql_connection.close()
    return books


def find_book(look_book) -> Books:
    found_book = []
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('SELECT * FROM books WHERE name = ?', (look_book["name"],))
    result = sql_cursor.fetchall()
    if len(result) > 0:
        found_book = [{'name': row[0], 'author': row[1], 'read': row[2] == 1} for row in result]
        print(found_book)
    sql_connection.close()
    return found_book


def mark_book_as_read(found_book) -> Books:
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute("SELECT * FROM books WHERE name = ?", (found_book["name"],))
    sql_cursor.execute("UPDATE books SET read = 1 WHERE name = ?", (found_book["name"],))
    sql_connection.commit()
    sql_connection.close()
    updated_book = find_book(found_book)
    return updated_book


def delete_book(book_to_delete) -> Books:
    sql_cursor, sql_connection = connect_to_db()
    sql_cursor.execute('DELETE FROM books WHERE name = ?', (book_to_delete["name"],))
    sql_connection.commit()
    sql_connection.close()
    return book_to_delete