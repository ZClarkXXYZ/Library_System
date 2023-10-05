

library_books = []



def find_book(title):
    #returns the book's details if found
    for book in library_books:
        if book['title'] == title:
            return(book)
    print(title + ' not found!')
    return(False)   #book was NOT found

def return_book(title):
    #changes the availibility of book to True
    book = find_book(title)
    if book != False:
        if book['availability'] == False:
            book['availability'] = True
            return(True)    # #book was returned
        else:
            print('Book is not borrowed to be returned')
            return(False)   #book was NOT returned (it is not borrowed)
    return(False)   #book was NOT returned, because it was not found

def borrow_book(title):
    #changes the availibility of book to False
    book = find_book(title)
    if book != False:
        if book['availability'] == True:
            book['availability'] = False
            return(True)    # book was borrowed
        else:
            print('Book is currently not available to be borrowed')
            return(False)   # book was borrowed because it is not available
    return(False)   #book was NOT borrowed, because it was not found

def add_book(title, author):
    #adds a book to library_books
    newBook = {'title':title, 'author':author, 'availability':True}
    if not newBook in library_books:
        library_books.append(newBook)
        print(title + " is added to the library")
        return(True)
    return(False)

def testMain():
    add_book('Who r u', 'Bob')
    #print(library_books)
    print('Test: add_book')
    print(library_books == [{'title': 'Who r u', 'author': 'Bob', 'availability': True}])

    borrow_book('Who r u')
    print('Test: borrow_book')
    print(library_books == [{'title': 'Who r u', 'author': 'Bob', 'availability': False}])

    return_book('Who r u')
    print('Test: return_book')
    print(library_books == [{'title': 'Who r u', 'author': 'Bob', 'availability': True}])

    #print('Test: find_book')
    #print(('Who r u', 'Bob', True) == find_book('Who r u'))



if __name__ == '__main__':
    testMain()