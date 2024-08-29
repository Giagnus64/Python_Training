""" Storing and retrieving from a list"""
import json


def add_book(book):
    #get books
    current_books = get_books()
    #write new book
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
        book_list = json.loads(file.read())
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

