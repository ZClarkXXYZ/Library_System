

library_books = []

def find_book(title):
    #returns the book's details if found
    for book in library_books:
        if book['title'] == title:
            return(book['title'], book['author'], book['availability'])
    print(title + ' not found!')

def return_book(title):
    #changes the availibility of book to True
    for book in library_books:
        if book['title'] == title:
            book['availability'] = True
            return
    print(title + ' not found!')

def borrow_book(title):
    #changes the availibility of book to False
    for book in library_books:
        if book['title'] == title:
            book['availability'] = False
            return
    print(title + ' not found!')

def add_book(title, author):
    #adds a book to library_books

    newBook = {'title':title, 'author':author, 'availability':True}
    library_books.append(newBook)


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

    print('Test: find_book')
    print(('Who r u', 'Bob', True) == find_book('Who r u'))



if __name__ == '__main__':
    testMain()