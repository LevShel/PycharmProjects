BooksID = [50, 34, -1, -1, 2, 23, -1]
NewBooksID = []
ReturnedBooks = 0

for _ in range(10):
    ID = int(input('Enter book ID: '))
    BooksID.append(ID)

for ID in BooksID:
    if ID == -1:
        ReturnedBooks += 1
    else:
        NewBooksID.append(ID)

print('New list of issued books: ', NewBooksID)
print('Quantity of returned books: ', ReturnedBooks)