'''
 1. Write a program, which takes a year as input and
 returns message if this is a leap year or note.
 2. Please handle the exceptions which may arise is a user
 will enter non-numeric symbols.
'''

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

