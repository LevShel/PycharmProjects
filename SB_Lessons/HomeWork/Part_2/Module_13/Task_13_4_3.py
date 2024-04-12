# Задача 3. Простые числа
# Реализуйте класс-итератор Primes, который принимает максимальное число N и выдаёт все простые числа от 1 до N.
# Основной код:
# prime_nums = Primes(50)
# for i_elem in prime_nums:
#     print(i_elem, end=' ')
# Ожидаемый результат кода:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
import math


class Primes:
    def __init__(self, n: int) -> None:
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num) + 1)):
            if num % i == 0:
                return False
        return True

    def __next__(self) -> int:
        self.current += 1
        while not self.is_prime(self.current):
            self.current += 1
            if self.current > self.n:
                raise StopIteration
        if self.current > self.n:
            raise StopIteration
        return self.current


prime_nums = Primes(50)
for i_elem in prime_nums:
    print(i_elem, end=' ')
