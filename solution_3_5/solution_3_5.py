
'''
  1. Write a program that will take username and password,
checks if they are in registered users dictionary,
if they are present '-' print 'Access Granted',
if not '-' handle it using KeyError Eception handling.
  2. Raise RuntimeError and handle it if the name is empty.
  3. For registered user, which is logged - let him know
if their password has unacceptable symbols (non alphanumeric)
and propose to change it using a dialog.
'''


import getpass
import string

authorized_users = {
    'root': 'root123.',
    'John': 'John123.',
    'Michael': 'Michael123.',
    'Alice': 'Alice123.',
    'Raichel': 'Raichel123.'
}
while True:
    try:
        name = input('Please enter your name: ')
        if name == '':
            raise RuntimeError
        print('Hello, {}'.format(name))
        password = getpass.getpass('Please enter your password: ')
        if authorized_users[name] == password:
            print('Access Granted!')
            break
    except KeyError:
        print("There's no such user registered!")
    except RuntimeError:
        print('Empty names are considered as a breach try!')

for symbol in authorized_users[name]:
    if symbol in string.punctuation:
        new_password = getpass.getpass(
            'Your password has unacceptable symbol in it: {} Please change your password: '.format(symbol))
        authorized_users[name] = new_password
        print('Your password is successfully updated!')