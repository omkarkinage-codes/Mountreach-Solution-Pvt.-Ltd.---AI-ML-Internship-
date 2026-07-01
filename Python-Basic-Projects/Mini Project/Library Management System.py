# Project 2: Library Management System

# 1. Initial Library Database 
library_db = {
    "978-072-4": {
        "title": "Basic Mathematics",
        "author": "M.S.B.T.E",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
    "978-362-0": {
        "title": "Applied Science",
        "author": "M.S.B.T.E",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
    "978-731-1": {
        "title": "Engineering Mechanics",
        "author": "N.H. Dubey",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
    "978-158-5": {
        "title": "Basic Electronics",
        "author": "J.B. Gupta",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
    "978-370-5": {
        "title": "Programming in C",
        "author": "E. Balagurusamy",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
    "978-394-6": {
        "title": "Python Programming",
        "author": "Reema Thareja",
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    },
   
}

# Function to add new book to the library dictionary
def add_book():
    print("\nAdd New Book ")
    isbn = input("Enter ISBN: ").strip()

    if isbn in library_db:
        print("This ISBN already exists!")
        return

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    # Create new nested dictionary record
    library_db[isbn] = {
        "title": title,
        "author": author,
        "available": True,
        "borrower_name": None,
        "borrower_id": None,
        "due_date": None,
    }
    print(f"'{title}' added successfully!")

# 3. Function to issue a book to a student
def issue_book():
    print("\nIssue a Book ")
    isbn = input("Enter ISBN:- ").strip()

    if isbn in library_db:
        if library_db[isbn]["available"] == True:
            print("Book is available.")

            borrower_name = input("Enter Student Name:- ").strip()
            borrower_id = input("Enter Student ID:- ").strip()

            # Update book keys to mark it as borrowed
            library_db[isbn]["available"] = False
            library_db[isbn]["borrower_name"] = borrower_name
            library_db[isbn]["borrower_id"] = borrower_id
            library_db[isbn]["due_date"] = "30-June-2026"

            print("\nBook Issued Successfully! ")
            print(f"Title    : {library_db[isbn]['title']}")
            print("Due Date : 30-June-2026 (Return within 7 days)")
        else:
            print("This book is already borrowed by someone else!")
    else:
        print("Book does not exist in the catalog.")


# 4. Function to return a book back to library
def return_book():
    print("\n Return a Book ")
    isbn = input("Enter ISBN:- ").strip()

    if isbn in library_db:
        if library_db[isbn]["available"] == False:
            # Reset values back to original defaults
            library_db[isbn]["available"] = True
            library_db[isbn]["borrower_name"] = None
            library_db[isbn]["borrower_id"] = None
            library_db[isbn]["due_date"] = None

            print("\nBook Returned Successfully! ")
        else:
            print("This book is already sitting in the library.")
    else:
        print("Book does not exist in the catalog.")


# 5. Function to search books by keyword
def search_book():
    print("\nSearch Book ")
    keyword = (input("Enter Title or Author name to search: ").strip().lower())

    found = False

    for isbn, details in library_db.items():
        if (
            keyword in details["title"].lower()
            or keyword in details["author"].lower()
        ):
            print(f"\nISBN      : {isbn}")
            print(f"Title     : {details['title']}")
            print(f"Author    : {details['author']}")
            if details["available"]:
                print("Status: Available")
            else:
                print(f"Status: Issued to {details['borrower_name']}")
            found = True

    if not found:
        print("No matches found.")


# 6. Function to display all books
def view_catalog():
    print("\nLibrary Catalog ")
    for isbn, details in library_db.items():
        if details["available"]:
            status = "Available"
        else:
            status = "Issued"
        print(f"ISBN: {isbn} | Title: {details['title']} | Author: {details['author']} | Status: {status}")


# 7. Main Menu Driver Loop
while True:
    print("\nLIBRARY MANAGEMENT SYSTEM ")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All")
    print("6. Exit")

    choice = input("Enter choice (1-6):- ").strip()

    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        search_book()
    elif choice == "5":
        view_catalog()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a number from 1 to 6.")