price = int(input('Enter price: '))
bank = int(input('Enter your balance: '))
if bank >= price:
  bank -= price
  print('Your current balance is:',bank)
  print('Course succesfully byued.')
  print('Have a nice day!')
else:
  bank -= price
  print('You need more money. Add',bank*(-1))