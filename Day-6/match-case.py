# import random

# numer = random.randint(0, 1)
#
# match numer:
#     case 1:
#         print('Heads')
#     case 0:
#         print('Tails')

# --------------------------------------------
# week_day = input('What is Day Today: ').capitalize()
#
# match week_day:
#     case 'Monday':
#         print('Today is Monday')
#
#     case 'Tuesday':
#         print('Today is Friday')


num1 = int(input())
num2 = int(input())
symbol = input()

match symbol:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)


