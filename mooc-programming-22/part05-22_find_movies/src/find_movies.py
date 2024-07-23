# Write your solution here
def find_movies(database: list, search_term: str) -> dict:
    found = []
    for movie in database:
        if search_term.lower() in movie['name'].lower():
            found.append(movie)
    return found

if __name__ == "__main__":
    

    my_movies = find_movies(database, "python")
    print(my_movies)
