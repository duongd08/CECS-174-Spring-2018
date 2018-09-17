#This lab is done by Daniel Duong and Cameron Kovacik.

interstate = int(input('Please enter the interstate number:'))

direction = interstate % 2

size = interstate % 5

last_two_digits = interstate % 100

first_digit = interstate // 100


if 0 < interstate <= 99:
    if (interstate % 2 == 0):
        print('Interstate', interstate, 'is a long-distance arterial highway oriented east-west.')

    else:
        print('Interstate', interstate, 'is a long-distance arterial highway oriented north-south.')

if 999 >= interstate >= 100:
    if (first_digit % 2 == 0):
        print('Interstate', interstate, 'is a circumfirential highway', 'of Interstate', last_two_digits)

    else:
        print('Interstate', interstate, 'is a spur highway', 'of Interstate', last_two_digits)




