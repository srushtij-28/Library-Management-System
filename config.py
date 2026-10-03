import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

BOOK_FILE = os.path.join(DATA_DIR, "books.json")
MEMBER_FILE = os.path.join(DATA_DIR, "members.json")
TRANSACTION_FILE = os.path.join(DATA_DIR, "transactions.json")

LOAN_DAYS = 14

TRANSACTION_STATUS_ISSUED = "Issued"
TRANSACTION_STATUS_RETURNED = "Returned"
