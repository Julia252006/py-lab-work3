
Brain Academy. Python Course. Laboratory Work #3

Laboratory Work #3.4.

1. Write a program, which takes a year as input and
 returns message if this is a leap year or note.
2. Please handle the exceptions which may arise is a user
 will enter non-numeric symbols.

Here is its solution code:

```python 

try:
    year = int(input('Please, enter the year:\n'))
except ValueError:
    print('Not a number passed')

if (year % 4 == 0) and (year % 100!= 0) or (year % 400 == 0):
    print ('Leap year is: ()'.format(year))
    print('It is a leap! 366 day in year!\n')
else:
    print('It is not a leap! 365 day in a year!:\n')
    for item in (year + 1, year + 2, year + 3, year - 1, year - 2, year - 3):
        if (item % 4 == 0) and (item % 100 != 0) or (item % 400 == 0):
            print('The closest leap year is: {}'.format(item))
            break
print('all leap_years in user defined year_range')


start = None
end = None
try:
    start = int(input('Please, enter start year:\n'))
    end = int(input('Please, enter end year:\n'))
except ValueError:
    print('Not a number passed!')

leaps = []
for x in range(start, end +1):
    if (x % 4 == 0) and (x % 100 !=0) or (x % 400 == 0):
        leaps.append(x)

print(leaps)
```

Brain Academy. Python Course. Laboratory Work #3

Laboratory Work #3.5.

  1. Write a program that will take username and password,
checks if they are in registered users dictionary,
if they are present '-' print 'Access Granted',
if not '-' handle it using KeyError Eception handling.
  2. Raise RuntimeError and handle it if the name is empty.
  3. For registered user, which is logged - let him know
if their password has unacceptable symbols (non alphanumeric)
and propose to change it using a dialog.

Here is its solution code:

```python 
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

```