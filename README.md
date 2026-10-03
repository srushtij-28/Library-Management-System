# Library Management System

A modular Python-based Library Management System for managing books,
members, and book borrowing transactions.

## Features

### Book Management

- Add books
- View books
- Search books
- Delete books
- Update book quantity
- Track available copies

### Member Management

- Add members
- View members
- Search members
- Deactivate members

### Transactions

- Issue books
- Return books
- Track due dates
- Track overdue days
- View transaction history
- View member borrowing history
- View currently issued books

### Reports

- Total book copies
- Available copies
- Issued copies
- Total members
- Active members
- Total transactions
- Book category report

## Technologies

- Python
- JSON
- File Handling
- Datetime
- Modular Programming

## Project Structure

library-management-system/
│
├── main.py
├── config.py
├── storage.py
├── utils.py
├── book_manager.py
├── member_manager.py
├── transaction_manager.py
├── report_manager.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── transactions.json
│
└── README.md

## How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/library-management-system.git
