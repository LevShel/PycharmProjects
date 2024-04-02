# В библиотеке есть список ID книг.
# Если книга выдана, то пишется ID, если книгу вернули, то пишется -1.
# Задача: нужно выдать 10 книг, но часть из них должны быть вернувшимися (т.е. -1).
# Необходимо вывести новый список ID выданных (исходный+введённый) книг и посчитать количество выданных за всё время книг.

# Исходный список
BooksID = [50, 34, -1, -1, 2, 23, -1]

# Новый пустой список выданных книг и количество вернувшмхся
NewBooksID = []
ReturnedBooks = 0

# Добавление новых книг
for _ in range(10):
    ID = int(input('Enter book ID: '))
    BooksID.append(ID)

# Подсчёт вернувшихся и формирование списка выданных
for ID in BooksID:
    if ID == -1:
        ReturnedBooks += 1
    else:
        NewBooksID.append(ID)

# Вывод результата
print('New list of issued books: ', NewBooksID)
print('Quantity of returned books: ', ReturnedBooks)