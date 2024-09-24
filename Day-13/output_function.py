import functions

# def Class(student_name, roll_number):
#     name = student_name
#     roll = roll_number
#     print(name, roll)
#
#
#
# class_student = Class('Hasnain', 303)
#
# print(class_student)


# ---------------------------------------------

# len_name = len('nsodnkjwe feowenfowjefb pijfbowejf')

# def print_name(f_name, s_name):
#     result = f_name + " " + s_name
#     return result
#
#
# full_name = print_name('Muhammad', 'Ahmad')
#
# print(full_name)

# ----------------------------------------------------

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     leap_year = is_leap(year)
#     if leap_year and month == 2:
#         print('This year is a leap year')
#         return 29
#     if leap_year:
#         print('This year is a leap year')
#         return month_days[month - 1]
#     else:
#         return month_days[month - 1]
#
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# ------------------------------------------------------------------------------

name = functions.print_name('muhammad ', 'ahmad')
print(name)
