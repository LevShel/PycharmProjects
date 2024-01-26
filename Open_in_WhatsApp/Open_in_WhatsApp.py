import webbrowser

# Шапка
name_of_programm = 'Open dialog in WhatsApp'
print('+', '-'*(len(name_of_programm)), '+\n|', name_of_programm, '|\n+', '-'*(len(name_of_programm)-8), 'by ШелЛ +\n')

print("You can write the phone number to open chat in WhatsApp.")
print("\nChoose your variant:")
print("1. Russia")
print("2. Armenia")
print("3. Israel")

choise = input("\nEnter 1...3: ")

if choise == '1':
    var = input("Enter phone number: +7 ")
    phone_number = '7' + var
    webbrowser.open(f"https://api.whatsapp.com/send?phone={phone_number}")
elif choise == '2':
    var = input("Enter phone number: +374 ")
    phone_number = '374' + var
    webbrowser.open(f"https://api.whatsapp.com/send?phone={phone_number}")
elif choise == '3':
    var = input("Enter phone number: +972 ")
    phone_number = '972' + var
    webbrowser.open(f"https://api.whatsapp.com/send?phone={phone_number}")
else:
    print("Error/ Please, choose 1/2/3.")
