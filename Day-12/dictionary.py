# my_dict = {1: 'mobile',
#            'version': '16',
#            'color': 'black',
#            'phone_number': 3353076462
# }
#
# #
# # student[0] = 'Muhammad'
# # print(student[0])
# print(my_dict)
#
# my_dict['version'] = '3.12'
#
# print(my_dict)


#
# print(universities)

# student_marks = {
#     'Hasnain': 90
# }

# students = ['Hasnain', 'Ahmad', 'Hassan']
#
# for i, student in enumerate(students):
#     print(student)
#     print(i)


# universities = {
#     'UCP': 'Lahore',
#     'Quid-Azam': 'Islamabad',
#     'IIUI': 'Islamabad',
#     'Gomal': 'Dera ISmail Khan'
# }
#
# for key, value in universities.items():
#     print(key, value)

#
# student_scores = {
#     "Hamza": 81,
#     "Ahmad": 78,
#     "Usman": 99,
#     "Zubair": 74,
#     "Hadi": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
# print(student_scores)
#
# student = input('Enter the name of the student: ')
# score = student_scores[student]
# if score > 90:
#     student_grades[student] = 'outstanding'
# elif score > 80:
#     student_grades[student] = 'Exceeds'
# elif score > 70:
#     student_grades[student] = 'Accpetable'
# else:
#     student_grades[student] = 'Fail'

# 🚨 Don't change the code below 👇
# print(student_grades)

# --------------------------------------------------------------------------------------------

# market = {
#     'fruits': ['Mango', 'Apple', 'Orange'],
#     'makeup': [],
#     'vegitable': ['Alo',' tomato']
# }
#
# print(market)

# skill_up = {
#     'Digital Markiting': {
#         'Teacher Name': '',
#         'Students': [],
#         'Course Outline': """
#
#         """,
#
#     },
#     'AI': {
#         'Teacher Name': [''],
#         'Students': [],
#         'Course Outlier': """
#
#         """
#     }
# }

#
# city_visit = {
#     'Islamabad': {
#         'Location': [],
#         'Visit': 10,
#     }
# }
#
# location = input('Enter location: ').split()
#
# city_visit['Islamabad']['Location'].append(location)
#
# print(city_visit)

# Country = [
#     {
#         'France': [''],
#         'Visited': 10
#     },
#     {
#         'Germany': ['Berlin', ],
#         'Visited': 9
#     }
#
# ]
#
# print(Country[0])


# -----------------------------------------------------------

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# # to be added to the travel_log. 👇
#
# def add_new_country(country_name, visited_number, visited_cities):
#     new_country = {}
#     new_country["country"] = country_name
#     new_country["visits"] = visited_number
#     new_country["cities"] = visited_cities
#     print(new_country)
#     travel_log.append(new_country)
#
#
# # 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


