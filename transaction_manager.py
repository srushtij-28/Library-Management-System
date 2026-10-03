from config import (
    BOOK_FILE,
    MEMBER_FILE,
    TRANSACTION_FILE,
    LOAN_DAYS,
    TRANSACTION_STATUS_ISSUED,
    TRANSACTION_STATUS_RETURNED
)

from storage import load_data, save_data

from utils import (
    generate_id,
    find_by_id,
    current_date,
    date_after_days,
    days_between
)


def issue_book():
    books = load_data(BOOK_FILE)
    members = load_data(MEMBER_FILE)
    transactions = load_data(TRANSACTION_FILE)

    if not books:
        print("No books available.")
        return

    if not members:
        print("No members registered.")
        return

    member_id = input("Enter Member ID: ").strip()

    member = find_by_id(members, member_id)

    if not member:
        print("Member not found.")
        return

    if not member["active"]:
        print("This member is inactive.")
        return

    book_id = input("Enter Book ID: ").strip()

    book = find_by_id(books, book_id)

    if not book:
        print("Book not found.")
        return

    if book["available"] <= 0:
        print("This book is currently unavailable.")
        return

    for transaction in transactions:
        if (
            transaction["book_id"] == book["id"]
            and transaction["member_id"] == member["id"]
            and transaction["status"] == TRANSACTION_STATUS_ISSUED
        ):
            print("This member already has this book.")
            return

    transaction = {
        "id": generate_id(transactions, "TX"),
        "book_id": book["id"],
        "book_title": book["title"],
        "member_id": member["id"],
        "member_name": member["name"],
        "issue_date": current_date(),
        "due_date": date_after_days(LOAN_DAYS),
        "return_date": None,
        "status": TRANSACTION_STATUS_ISSUED
    }

    transactions.append(transaction)

    book["available"] -= 1

    save_data(TRANSACTION_FILE, transactions)
    save_data(BOOK_FILE, books)

    print("\nBook issued successfully.")
    print(f"Transaction ID: {transaction['id']}")
    print(f"Due Date: {transaction['due_date']}")


def return_book():
    books = load_data(BOOK_FILE)
    transactions = load_data(TRANSACTION_FILE)

    transaction_id = input(
        "Enter Transaction ID: "
    ).strip()

    transaction = find_by_id(
        transactions,
        transaction_id
    )

    if not transaction:
        print("Transaction not found.")
        return

    if transaction["status"] == TRANSACTION_STATUS_RETURNED:
        print("This book has already been returned.")
        return

    book = find_by_id(
        books,
        transaction["book_id"]
    )

    if book:
        book["available"] += 1

    return_date = current_date()

    transaction["return_date"] = return_date
    transaction["status"] = TRANSACTION_STATUS_RETURNED

    overdue_days = days_between(
        transaction["due_date"],
        return_date
    )

    if overdue_days < 0:
        overdue_days = 0

    transaction["overdue_days"] = overdue_days

    save_data(TRANSACTION_FILE, transactions)
    save_data(BOOK_FILE, books)

    print("\nBook returned successfully.")

    if overdue_days > 0:
        print(f"Overdue by {overdue_days} day(s).")
    else:
        print("Book returned on time.")


def view_transactions():
    transactions = load_data(TRANSACTION_FILE)

    if not transactions:
        print("No transactions found.")
        return

    print("\n" + "=" * 90)
    print("LIBRARY TRANSACTIONS")
    print("=" * 90)

    for transaction in transactions:
        print(f"ID          : {transaction['id']}")
        print(f"Book        : {transaction['book_title']}")
        print(f"Member      : {transaction['member_name']}")
        print(f"Issue Date  : {transaction['issue_date']}")
        print(f"Due Date    : {transaction['due_date']}")
        print(f"Return Date : {transaction['return_date']}")
        print(f"Status      : {transaction['status']}")

        if "overdue_days" in transaction:
            print(
                f"Overdue     : "
                f"{transaction['overdue_days']} day(s)"
            )

        print("-" * 90)


def member_history():
    transactions = load_data(TRANSACTION_FILE)

    member_id = input("Enter Member ID: ").strip()

    results = [
        transaction
        for transaction in transactions
        if transaction["member_id"].lower()
        == member_id.lower()
    ]

    if not results:
        print("No transaction history found.")
        return

    print("\nMember History")

    for transaction in results:
        print(
            f"{transaction['id']} | "
            f"{transaction['book_title']} | "
            f"{transaction['issue_date']} | "
            f"{transaction['status']}"
        )


def currently_issued():
    transactions = load_data(TRANSACTION_FILE)

    results = [
        transaction
        for transaction in transactions
        if transaction["status"] == TRANSACTION_STATUS_ISSUED
    ]

    if not results:
        print("No books are currently issued.")
        return

    print("\nCurrently Issued Books")

    for transaction in results:
        print(
            f"{transaction['id']} | "
            f"{transaction['book_title']} | "
            f"{transaction['member_name']} | "
            f"Due: {transaction['due_date']}"
        )
