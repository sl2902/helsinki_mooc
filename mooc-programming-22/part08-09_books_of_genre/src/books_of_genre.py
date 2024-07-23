# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

    ##STUB:# This enables easy printing of a Book object
    def __repr__(self):
        return f"{self.name} ({self.author}), {self.year} - genre: {self.genre}"


# -----------------------------
# Write your solution here
# -----------------------------
def older_book(book1: Book, book2: Book) -> None:
    if book1.year < book2.year:
        print(f'{book1.name} is older, it was published in {book1.year}')
    elif book2.year < book1.year:
        print(f'{book2.name} is older, it was published in {book2.year}')
    else:
        print(f'{book1.name} and {book2.name} were published in {book1.year}')

def books_of_genre(books: list, genre: str) -> list:
    return [book for book in books if genre == book.genre]


if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)

    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    books = [python, everest, norma, Book("The Snowman", "Jo Nesbø", "crime", 2007)]

    print("Books in the crime genre:")
    for book in books_of_genre(books, "crime"):
        print(f"{book.author}: {book.name}")
