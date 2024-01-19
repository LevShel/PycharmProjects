true_pin = '1234'

for attempt in range(1,4):
  pin = input('Enter pin: ')
  print()
  if pin == true_pin:
    print('Success!\n')
    break
  print('Pin is wrong! You have ', (3-attempt),' attempts. \n')
else:
  print('Your card is blocked! Try later.')