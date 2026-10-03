from config import BOOK_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_book():
    books = load_data(BOOK_FILE)

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    category = input("Enter category: ").strip()

    if not title or not author:
        print("Title and author are required.")
        return

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity.")
        return

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return

    book = {
        "id": generate_id(books, "B"),
        "title": title,
        "author": author,
        "category": category,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)

    save_data(BOOK_FILE, books)

    print("\nBook added successfully.")
    print(f"Book ID: {book['id']}")


def view_books():
    books = load_data(BOOK_FILE)

    if not books:
        print("No books found.")
        return

    print("\n" + "=" * 80)
    print("BOOK LIST")
    print("=" * 80)

    for book in books:
        print(f"ID        : {book['id']}")
        print(f"Title     : {book['title']}")
        print(f"Author    : {book['author']}")
        print(f"Category  : {book['category']}")
        print(f"Quantity  : {book['quantity']}")
        print(f"Available : {book['available']}")
        print("-" * 80)


def search_books():
    books = load_data(BOOK_FILE)

    keyword = input(
        "Enter book ID, title, author, or category: "
    ).strip().lower()

    results = [
        book
        for book in books
        if keyword in book["id"].lower()
        or keyword in book["title"].lower()
        or keyword in book["author"].lower()
        or keyword in book["category"].lower()
    ]

    if not results:
        print("No books found.")
        return

    print("\nSearch Results")

    for book in results:
        print(
            f"{book['id']} | "
            f"{book['title']} | "
            f"{book['author']} | "
            f"Available: {book['available']}"
        )


def delete_book():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ").strip()

    book = find_by_id(books, book_id)

    if not book:
        print("Book not found.")
        return

    if book["available"] != book["quantity"]:
        print("Cannot delete a book that is currently issued.")
        return

    books.remove(book)

    save_data(BOOK_FILE, books)

    print("Book deleted successfully.")


def update_book_quantity():
    books = load_data(BOOK_FILE)

    book_id = input("Enter Book ID: ").strip()

    book = find_by_id(books, book_id)

    if not book:
        print("Book not found.")
        return

    try:
        new_quantity = int(
            input("Enter new total quantity: ")
        )
    except ValueError:
        print("Invalid quantity.")
        return

    issued = book["quantity"] - book["available"]

    if new_quantity < issued:
        print(
            f"Quantity cannot be less than currently issued books: {issued}"
        )
        return

    book["quantity"] = new_quantity
    book["available"] = new_quantity - issued

    save_data(BOOK_FILE, books)

    print("Book quantity updated successfully.")
