from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
"""
menu_selection = ['a','q','l','r','d']
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == "a":
            prompt_to_add_book()
        elif user_input == 'l':
            to_print = database.get_books()
            print_to_user(to_print)
        elif user_input == 'r':
            prompt_to_mark()
        elif user_input == 'd':
            prompt_to_delete()
        elif user_input not in menu_selection:
            print(f"{user_input} is not a valid choice. Please try again")

        user_input = input(USER_CHOICE)
#ask user to add book
def prompt_to_add_book():
    book_title = input("Enter book title: ")
    book_author = input("Enter book author: ")
    book_read = input("Have you read this book? (y/n): ")
    if book_read == 'y':
        book_read = True
    else:
        book_read = False
    book_to_add = {"name": book_title, "author": book_author, "read":book_read}
    if database.find_book(book_to_add):
        print_to_user(f"{book_to_add} is already added. Please use the 'r' command to mark a book as read.")
    else:
        user_message = database.add_book(book_to_add)
        print_to_user(user_message)
    return True

#mark book as read
def prompt_to_mark():
    #prompt for book title
    book_name = input("Enter the name of the book you would like to mark as read: ")
    book_author = input("Enter the author of the book you would like to mark as read: ")
    found_book = database.find_book({"name": book_name, "author":book_author})
    if found_book and found_book["read"]:
        print_to_user(f"{found_book["name"]} by {found_book["author"]} is already marked as read.")
    elif found_book:
        book_marked = database.mark_book_as_read(found_book)
        print_to_user(f"{book_marked["name"]} is marked as read.")
    else:
        print_to_user(f"{book_name} by {book_author} was not found. Please try again.")
    return True

def prompt_to_delete():
    #prompt for book title
    book_name = input("Enter the name of the book you would like to delete: ")
    book_author = input("Enter the author of the book you would like to delete: ")
    found_book = database.find_book({"name": book_name, "author":book_author})
    if found_book:
        confirm = input(f"Are you sure you want to delete {found_book["name"]} by {found_book["author"]}? (y/n")
        if confirm == 'y':
            deleted_book = database.delete_book(found_book)
            print_to_user(f"{deleted_book["name"]} by {deleted_book["author"]} was deleted.")
        else:
            print_to_user(f"{book_name} by {book_author} was NOT deleted.")
    else:
        print_to_user(f"{book_name} by {book_author} was not found. Please try again.")
    return True

def print_to_user(print_statement):
    print(print_statement)
    return True

menu()