# # names = ['Hasnain', 'Ahmad', 'Muhammad', 'Hamza']
# #
# # for x in names:
# #     print(x)
#
# # library = ['English', 'Urdu', 'Maths', 'Physics']
# #
# # for book in library:
# #     print(book)
#
# # -----------------------------------------------
#
# # library = ['English', 'Urdu', 'Maths', 'Physics']
# #
# # for num in range(len(library)):
# #     # print(library[num])
# #     if library[num] == 'Maths':
# #         print(num)
#
# # total_num = 0
# # for num in range(1, 101):
# #     total_num += num
#
# # -----------------------------------------------------
#
# # Average Student Height
#
# students_height = input('Enter Students Height separate each of them with spaces: ').split()
#
# for _ in range(0, len(students_height)):
#     students_height[_] = float(students_height[_])
#
# # print(students_height)
#
# # sum of all the heights of students / total num of h
#
# total_students = 0
#
# for _ in students_height:
#     total_students += 1
#
# # print(total_students)
#
#
# total_height = 0
#
# for height in students_height:
#     # print(height)
#     total_height += height
#
# # print(total_height)
#
# average = total_height / total_students
#
# print(f'The average height of each student is {average}')

# --------------------------------------------------------------------------

# students_height = input('Enter Students Height separate each of them with spaces: ').split()
#
# for _ in range(0, len(students_height)):
#     students_height[_] = float(students_height[_])
#
# total_students = len(students_height)
# total_height = sum(students_height)
#
# average = round(total_height / total_students, 2)
#
# print(average)

# ------------------------------------------------------------------------

# students = ['Ahmad', 'Hassan', 'ahsan']

# name = 'Hasnain'
#
# new_name = ''
#
# for i in name:
#     if i == 'n':
#         new_name = name.replace(i, 'p')
#
# print(name)
# print(new_name)


# for i in range(2, 100, 2):
#     print(i)


# --------------------------------------------------------------------------
numer = int(input('Enter any number: '))

# for i in range(0, numer):
#
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('Fizzbuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     print(i)
