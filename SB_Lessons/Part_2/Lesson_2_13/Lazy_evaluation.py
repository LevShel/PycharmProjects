class Fibonacci:
    def __init__(self, number):
        self.counter = 0
        self.current_value = 0
        self.next_value = 1
        self.number = number

    def __iter__(self):
        self.counter = 0
        self.current_value = 0
        self.next_value = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration
            self.current_value, self.next_value = self.next_value, self.current_value + self.next_value
        return self.current_value


fib_iterator = Fibonacci(9999999999)

print(8 in fib_iterator)  # Проверяем, есть ли число 8 в последовательности
