
def add_book(books, title, author, year):
    books.append({"title": title, "author": author, "year": year})
    print(f"Book '{title}' added successfully.")

def search_book(books, title):
    for book in books:
        if book["title"] == title:
            return book
    return None

def display_inventory(books):
    print("\nLibrary Inventory:")
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

def main():
    books = []
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. Display Inventory")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = input("Enter publication year: ")
            add_book(books, title, author, year)
        elif choice == 2:
            title = input("Enter book title to search: ")
            book = search_book(books, title)
            if book:
                print(f"Book found: {book['title']} by {book['author']} ({book['year']})")
            else:
                print("Book not found.")
        elif choice == 3:
            display_inventory(books)
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

main()