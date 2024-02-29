# Задача 3. Пакеты
# При работе с сервером мы кодируем сообщение и отправляем его в виде пакетов информации.
# Их количество равно N. Допустим, каждый пакет содержит четыре числа, каждое из которых
# равно нулю или единице. Эти числа называются битами. Иногда в кодировке сообщения
# встречаются ошибки, и в пакете эта ошибка обозначается числом -1. Если таких ошибок
# не больше одной, то этот пакет мы целиком добавляем в список для декодирования,
# а иначе отбрасываем.
# Напишите программу, которая будет обрабатывать полученные пакеты и выведет на экран
# итоговое сообщение для декодирования, а также количество ошибок в нём и количество
# необработанных пакетов.
#
# Пример:
# Кол-во пакетов: 3
#
# Пакет номер 1
# 1 бит: 1
# 2 бит: 0
# 3 бит: -1
# 4 бит: 1
#
# Пакет номер 2
# 1 бит: -1
# 2 бит: -1
# 3 бит: 1
# 4 бит: 1
# Много ошибок в пакете.
#
# Пакет номер 3
# 1 бит: 0
# 2 бит: 1
# 3 бит: 1
# 4 бит: 1
#
# Полученное сообщение: [1, 0, -1, 1, 0, 1, 1, 1]
# Кол-во ошибок в сообщении: 1
# Кол-во потерянных пакетов: 1

def add_new_pack(num):
    packs = []
    lost_packs = 0
    message_errors = 0
    for pack in range(num_packs):
        print(f'\nPack number {pack + 1}')
        new_pack = []
        for i in range(4):
            bit = input(f'{i + 1} bit: ')
            new_pack.append(bit)
        if new_pack.count('-1') == 0:
            packs.extend(new_pack)
        elif new_pack.count('-1') == 1:
            packs.extend(new_pack)
            message_errors += 1
        elif new_pack.count('-1') > 1:
            print('A lot of errors in pack.')
            lost_packs += 1
    return packs, lost_packs, message_errors


num_packs = int(input('Num of packs: '))
packs, message_errors, lost_packs = add_new_pack(num_packs)
print(f'\nThe received message: {packs}\n'
      f'Num of errors in message: {message_errors}\n'
      f'Num of lost packs: {lost_packs}')
