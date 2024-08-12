MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

def add_movie():
    title = input("Enter the movie title: ")
    if title == "":
        print("Title must be not be empty!")
        return
    director = input("Enter the movie director: ")
    if director == "":
        print("Director must be not be empty!")
        return
    year = input("Enter the movie release year: ")
    if year == "":
        print("Year must be not be empty!")
        return

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })

    print(f"{title} added successfully!")


# Create other functions for:
#   - listing movies
def list_movies():
    if len(movies) != 0:
        for movie in movies:
            print(movie['title'], movie['director'], movie['year'])
    else:
        print("You haven't added any movies yet!")
#   - finding movies
def find_movie_by_title(title):
    found_movies = []
    for movie in movies:
        if movie['title'] == title:
            found_movies.append(movie)
    return found_movies

def print_movies(movie_list):
    if len(movie_list) == 0 and len(movies) == 0:
        print ("You haven't added any movies yet!")
    elif len(movie_list) == 0:
        print(" No movies found with that search.")
    else:
        for movie in movie_list:
            print(f"Title:{movie['title']}, Directed By: {movie['director']}, Release Date: {movie['year']}")

def error_checker(check):
    if check == "":
        return False


def run_menu():
    # And another function here for the user menu
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == "a":
            add_movie()
        elif selection == "l":
            print_movies(movies)
        elif selection == "f":
            title = input("Enter the movie title: ")
            found_movies = find_movie_by_title(title)
            print_movies(found_movies)
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!

run_menu()
#adding code to change