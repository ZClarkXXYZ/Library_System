

from books import *
from members import *

def showAllBooks():
    allBooks = ''
    if library_books != []:
        for book in library_books:
            allBooks = allBooks +  ("Book Title: " + book['title'] + "      Author: " + book['author'] + "      Availability : " + str(book['availability']) + "\n")
        return(allBooks)
    else:
        return("No Books are in inventory")


def showAllMembers():
    allMembers = 'Current Members: \n'
    if library_members != []:
        for member in library_members:
            allMembers = allMembers + member + '\n'
        return(allMembers)
    else:
        return("No Members Registered!")

def inputNewBook():

    newTitle = input("Enter Title of New Book: ")
    newAuthor = input("Enter Author of New Book: ")
    add_book(newTitle, newAuthor)
    return

def displayMenu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Display all books.")
    print("6. Display all members.")
    print("7. Exit.")
    print("----------------------------")

def main():

    while True:
        displayMenu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            # Call function to add a new book
            inputNewBook()

        elif choice == "2":
            # Call function to register a new member
            newMember = input('Enter name of new library member: ')
            register_member(newMember)

        elif choice == "3":
            # Call function to borrow a book
            borrow_book(input('Enter title of book to borrow: '))

        elif choice == "4":
            # Call function to return a book
            borrow_return(input('Enter title of book to return: '))

        elif choice == "5":
            # Call function to display all books
            print(showAllBooks())

        elif choice == "6":
            # Call function to display all members
            print(library_members)
            # TODO: temporary solution. Fix to be more fancy later

        elif choice == "7":
            print("Thank you for using the Library Management System! Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == '__main__':
    main()
