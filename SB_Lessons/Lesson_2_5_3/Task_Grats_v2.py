while True:
    grats_template = input('Enter text of congratulation. '
                       'For name use {name}, for age use {age}: ')
    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print('Error! There is no one or more constructions {}.')

names_list = input('Enter a comma-separated list of names: ').split(', ')
age_str = input('Enter a space-separated list of ages: ')
ages = [int(i_number) for i_number in age_str.split()]

print()
for i_man in range (len(names_list)):
    print(grats_template.format(name=names_list[i_man], age=ages[i_man]))

people = [' '.join([names_list[i_man], str(ages[i_man])])
          for i_man in range(len(names_list))]

people_str = ', '.join(people)
print('\nBirthday people: ', people_str)