scores = [90, 98, 20, 87, 67]
#
# total_score = 0
#
# for i in scores:
#     total_score += i


# Syntax
# [expression for item in iterable if condition]


# total_score = [i for i in range(10)]
#
# print(total_score)

# numbers = [item for item in scores]
#
# print(numbers)



# total_index = []
#
# for i in range(10):
#     total_index.append(i)
#
# print(total_index)

# Without list comprehension
# squares = []
# for i in range(1, 6):
#     squares.append(i**2)
#
# print(squares)


# With list comprehension
# squares = [i**2 for i in range(1, 6)]
#
# print(squares)


fruits = ["apple", "orange", "banana", "coconut", ['ahmad', 'hassan', 'muhammad']]
# # uppercase_words = [fruit.upper() for fruit in fruits]
# #
# # print(uppercase_words)
#
# fruit_chars = [i for i in fruits[:4]]
# fruit_chars_2 = [i for i in fruits[4]]
# print(fruit_chars)
# print(fruit_chars_2)

students = ['Muhammad', 'Hasnain', 'Ahmad', 'Hassan']
# new_st = []
#
# for i in students:
#     if i.startswith('H'):
#         new_st.append(i)
#
# print(new_st)


# new_st = [i for i in students if i.startswith('H')]

# print(new_st)

# ----------------------------------------------------------------

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]

# positive_numbers = [x for x in numbers if x > 0]
# negative_numbers = [x for x in numbers if x < 0]
# even_numbers = [x for x in numbers if x % 2 == 0]
# odd_numbers = [x for x in numbers if x % 2 == 1]
#
# print(positive_numbers)
# print(negative_numbers)
# print(even_numbers)
# print(odd_numbers)


# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)



