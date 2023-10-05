# library_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import main  # Assuming main.py contains the functions for the library operations
from books import *
from members import *




def registermember():
    # Call the function to register a member
    #####messagebox.showinfo("Info", "Register member functionality here")
    name = simpledialog.askstring("Input", "Enter name of new member:")
    if name:  # Check if the user provided a title (didn't press cancel)
        if register_member(name):  # Using the function from members.py
            messagebox.showinfo("Success", name + " added successfully!")
        else:
            messagebox.showwarning("Warning", name + " is already registered")
    else:
        messagebox.showwarning("Warning", "Cancel adding of member. Name not given")
def borrowbook():
    # Call the function to borrow a book
    ############messagebox.showinfo("Info", "Borrow book functionality here")
    title = simpledialog.askstring("Input Return", "Enter the title of the book to borrow:")
    if title:  #(didn't press cancel)
        if borrow_book(title):  # Using the return_book function from books.py
            messagebox.showinfo("Success", "Book borrowed!")
        else:
            messagebox.showinfo("Error", "Book was not borrowed. Either it is currently unavailable, or title is wrong")
    else:
        messagebox.showwarning("Warning", "Book borrowing cancelled. Title was not provided")

def returnbook():
    # Call the function to return a book
    #########messagebox.showinfo("Info", "Return book functionality here")
    title = simpledialog.askstring("Input Return", "Enter the returning book's title:")
    if title:  #(didn't press cancel)
        if return_book(title):  # Using the return_book function from books.py
            messagebox.showinfo("Success", "Book returned!")
        else:
            messagebox.showinfo("Error", "Book was not returned. Either it is already is returned, or title is wrong")
    else:
        messagebox.showwarning("Warning", "Book return cancelled. Title was not provided")

def displaybooks():
    # Call the function to display all books
    messagebox.showinfo("Info", main.showAllBooks())

def displaymembers():
    # Call the function to display all members
    messagebox.showinfo("Info", main.showAllMembers())

def addbook():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            if add_book(title, author): # Using the function from books.py
                messagebox.showinfo("Success", "Book added successfully!")
            else:
                messagebox.showwarning("Warning", "Book addition cancelled. Book already in system.")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")

root = tk.Tk()
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=addbook)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=registermember)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrowbook)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=returnbook)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=displaybooks)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=displaymembers)
display_members_btn.pack(pady=10)



root.mainloop()