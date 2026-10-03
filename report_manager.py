from config import (
    BOOK_FILE,
    MEMBER_FILE,
    TRANSACTION_FILE,
    TRANSACTION_STATUS_ISSUED,
    TRANSACTION_STATUS_RETURNED
)

from storage import load_data


def library_statistics():
    books = load_data(BOOK_FILE)
    members = load_data(MEMBER_FILE)
    transactions = load_data(TRANSACTION_FILE)

    total_books = sum(
        book["quantity"]
        for book in books
    )

    available_books = sum(
        book["available"]
        for book in books
    )

    issued_books = total_books - available_books

    active_members = sum(
        1
        for member in members
        if member["active"]
    )

    returned_books = sum(
        1
        for transaction in transactions
        if transaction["status"]
        == TRANSACTION_STATUS_RETURNED
    )

    print("\n" + "=" * 50)
    print("LIBRARY STATISTICS")
    print("=" * 50)

    print(f"Total Book Copies : {total_books}")
    print(f"Available Copies  : {available_books}")
    print(f"Issued Copies     : {issued_books}")
    print(f"Total Members     : {len(members)}")
    print(f"Active Members    : {active_members}")
    print(f"Total Transactions: {len(transactions)}")
    print(f"Returned Books    : {returned_books}")


def category_report():
    books = load_data(BOOK_FILE)

    if not books:
        print("No books found.")
        return

    categories = {}

    for book in books:
        category = book["category"] or "Uncategorized"

        if category not in categories:
            categories[category] = 0

        categories[category] += book["quantity"]

    print("\nBook Category Report")

    for category, quantity in categories.items():
        print(f"{category}: {quantity} copies")
