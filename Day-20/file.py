# import demo
#
# print(demo.greet())

# file = open('ideas.txt')
# text = file.read()
# # print(text)
# file.close()
#
# print(text)

# file = open('ideas1.txt', 'w')
# text = file.write('Hi')
# print(text)
# file.close()


# with open('ideas1.txt', 'a') as t:
#     file = t.write('Hi their')
#     print(file)


# with open('ideas.txt', 'r') as file:
#     text = file.readlines()
#     print(text)


# Example 1: Writing User Data to a File
# Create a program that asks the user to input their name, age, and email, and then writes this information to a file named user_data.txt. Each new entry should be written on a new line.

# def user_data():
#     with open('user_data.txt', 'a') as file:
#         name = input('Enter Your Name: ')
#         age = int(input('Enter Your Age: '))
#         email = input('Enter Your Email: ')
#         text = file.write(f'Name: {name}, age {age}, email {email}\n')
#         print(text)
#
#
# user_data()

