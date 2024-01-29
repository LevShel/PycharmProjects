# Задача 3. Лотерея 2
# Напишите программу для немного усложнённой версии задачи про выигрышные билеты.
# Есть заранее известные номера билетов: 345, 19, 87, 1020 и 421
# (можете брать свои номера, не стесняйтесь).
# Теперь, билет считается выигрышным, если номер билета - трёхзначное число и оно делится на 5.
# Выведете в консоль сообщение для каждого выигрышного билета и количество победителей.

tickets = [345, 19, 87, 1020, 421, 555]

winners = 0
win_tickets = []

for ticket in tickets:
    if ticket % 5 == 0:
        ticket = str(ticket)
        if len(ticket) == 3:
            winners += 1
            win_tickets.append(ticket)

for win_ticket in win_tickets:
    print(f'Ticket {win_ticket} - win!')
print(f'There are: {winners} winners.')

#### Упрощённый код ####
# tickets = [345, 19, 87, 1020, 421, 555]
#
# win_tickets = [str(ticket) for ticket in tickets if ticket % 5 == 0 and len(str(ticket)) == 3]
#
# for win_ticket in win_tickets:
#     print(f'{win_ticket} - win!')
#
# print(f'There are: {len(win_tickets)} winners.')