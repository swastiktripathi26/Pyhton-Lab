count = 0
while count < 3:
    password = input('Enter password: ')
    if password == 'hello':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1

