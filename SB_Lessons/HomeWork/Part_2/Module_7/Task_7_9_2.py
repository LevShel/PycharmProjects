# Задача 2. Универсальная программа
# Что нужно сделать
# Напишите функцию, возвращающую список элементов итерируемого объекта
# (кортежа, строки, списка, словаря), у которых индекс — это простое число.
# Для проверки на простое число напишите отдельную функцию is_prime.
# Необязательное усложнение: сделайте так, чтобы основная функция состояла
# только из оператора return и так же возвращала список.
# Пример вызова функции:
# print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# Ответ в консоли: [2, 3, 5, 7]
# Пример вызова функции:
# print(crypto('О Дивный Новый мир!'))
# Ответ в консоли: ['Д', 'и', 'н', 'й', 'в', 'й', 'р']
# Советы и рекомендации
# Для нумерации элементов используйте функцию enumerate. Это позволит
# работать одинаково со всеми структурами данных.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def crypto(inp_command):
    list_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    string_original = 'О Дивный Новый мир!'
    tuple_original = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    dictionary_original = {0: 0, 1: 1, 2: 2, 3: 3, 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 8, 9: 9, 10: 10}
    list_crypto = list

    if inp_command == 1:
        list_crypto = [sym for idx, sym in enumerate(list_original) if is_prime(idx)]

    elif inp_command == 2:
        list_crypto = [sym for idx, sym in enumerate(string_original) if is_prime(idx)]

    elif inp_command == 3:
        list_crypto = [sym for idx, sym in enumerate(tuple_original) if is_prime(idx)]

    elif inp_command == 4:
        list_crypto = [dictionary_original[index] for index in dictionary_original if is_prime(index)]

    return list_crypto


while True:
    command = int(input('\nList -> List: 1\n'
                        'String -> List: 2\n'
                        'Tuple -> List: 3\n'
                        'Dictionary -> List: 4\n'
                        '>: '))
    print(crypto(command))
