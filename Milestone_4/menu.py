from app import books

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''

def print_best_books(sort_method=str | None) -> None:
    if sort_method == 'ascending':
        mod = 1
    else:
        mod = -1
    best_books = sorted(books, key= lambda x: x.rating * mod)[:10]
    for book in best_books:
        print(book)
    return None

def sort_by_price_books(sort_method=str | None) -> None:
    if sort_method == 'ascending':
        mod = 1
    else:
        mod = -1
    cheapest_first = sorted(books, key= lambda x: x.price * mod) [:10]
    for book in cheapest_first:
        print(book)
    return None

books_generator = (x for x in books)


def get_next_book():
    # logger.debug('Getting next book from generator of all books...')
    print(next(books_generator))
    return None

user_choices = {
    'b': print_best_books,
    'c': sort_by_price_books,
    'n': get_next_book
}

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
         #logger.debug('User did not choose to exit program.')
        if user_input in ('b', 'c', 'n'):
            user_choices[user_input]()
        else:
            print('Please choose a valid command.')
        user_input = input(USER_CHOICE)
    # logger.debug('Terminating program...')


menu()
