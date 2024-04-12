items = [10, 20, 30]

iterator = items.__iter__()
print(iterator)  # <list_iterator object at ...>

iterator = iter(items)
print(iterator)  # <list_iterator object at ...>

for elem in iterator:
    print(elem, end=' ')  # 10 20 30
print()

iterator = iter(items)
print(iterator.__next__())  # 10
print(next(iterator))  # 20
