import os

from config import (
    DATA_DIR,
    BOOK_FILE,
    MEMBER_FILE,
    TRANSACTION_FILE
)

from storage import save_data

from book_manager import (
    add_book,
    view_books,
    search_books,
    delete_book,
    update_book_quantity
)

from member_manager import (
    add_member,
    view_members,
    search_members,
    deactivate_member
)

from transaction_manager import (
    issue_book,
    return_book,
    view_transactions,
    member_history,
    currently_issued
)

from report_manager import (
    library_statistics,
    category_report
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [
        BOOK_FILE,
        MEMBER_FILE,
        TRANSACTION_FILE
    ]

    for filename in files:
        if not os.path.exists(filename):
            save_data(filename, [])


def show_menu():
    print("\n")
    print("=" * 60)
    print("          LIBRARY MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\nBOOK MANAGEMENT")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Books")
    print("4. Delete Book")
    print("5. Update Book Quantity")

    print("\nMEMBER MANAGEMENT")
    print("6. Add Member")
    print("7. View Members")
    print("8. Search Members")
    print("9. Deactivate Member")

    print("\nTRANSACTIONS")
    print("10. Issue Book")
    print("11. Return Book")
    print("12. View Transactions")
    print("13. Member History")
    print("14. Currently Issued Books")

    print("\nREPORTS")
    print("15. Library Statistics")
    print("16. Category Report")

    print("\n17. Exit")

    print("=" * 60)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_books()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            update_book_quantity()

        elif choice == "6":
            add_member()

        elif choice == "7":
            view_members()

        elif choice == "8":
            search_members()

        elif choice == "9":
            deactivate_member()

        elif choice == "10":
            issue_book()

        elif choice == "11":
            return_book()

        elif choice == "12":
            view_transactions()

        elif choice == "13":
            member_history()

        elif choice == "14":
            currently_issued()

        elif choice == "15":
            library_statistics()

        elif choice == "16":
            category_report()

        elif choice == "17":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
