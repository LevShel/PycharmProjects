def ask_user(question,
             compliant='Wrong answer. Please type "Yes" or "No"',
             retries=4):
    while True:
        answer = input(question).lower()
        if answer == 'yes':
            return 1
        if answer == 'no':
            return 0
        retries -= 1
        if retries == 0:
            print('There is no retries.')
            break
        print(compliant)
        print(f'You have {retries} retries.')


ask_user('You want exit?\n'
         '>: ')
ask_user('Delete file?\n'
         '>: ',
         'New compliant')
ask_user('Save file?\n'
         '>: ', retries=2)
