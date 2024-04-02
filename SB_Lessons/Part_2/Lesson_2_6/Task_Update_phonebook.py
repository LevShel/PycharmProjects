phonebook = {
    'Ivan' : 100,
    'Peter' : 200,
    'Alice' : 300
}

other_phonebook = {
    'Igor' : 400,
    'Peter' : 222,
    'Elen' : 500
}

print('1st PB: ', phonebook)
print('2nd PB: ', other_phonebook)

phonebook.update(other_phonebook)
print('Updated 1st PB:', phonebook)