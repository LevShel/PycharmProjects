import random


class RandomNumbers:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return random.randint(0, 10)
        else:
            raise StopIteration


my_iter = RandomNumbers(limit=5)
for num in my_iter:
    print(num)
