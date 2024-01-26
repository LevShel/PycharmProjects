import webbrowser

# Шапка
name_of_programm = 'Open dialog in Telegram'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')

# Меню
print("You can write the phone number to open chat in Telegram.")
print("\nChoose your variant:")
print("1. Nickname")
print("2. Russia")
print("3. Armenia")
print("4. Israel")

# Выбор действия/страны
choise = input("\nEnter 1...4: ")

if choise == '1':
    var = input("Enter the nickname: ")
    webbrowser.open(f"https://t.me/{var}")
elif choise in {'2', '3', '4'}:
    country_codes = {'2': '+7', '3': '+374', '4': '+972'}
    var = input(f"Enter phone number: {country_codes[choise]} ")
    phone_number = country_codes[choise] + var
    webbrowser.open(f"https://t.me/{phone_number}")
else:
    print("Error/ Please, choose 1/2/3/4.")
