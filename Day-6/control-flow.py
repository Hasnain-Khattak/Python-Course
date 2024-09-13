import random
# age = int(input('Enter Your Age: '))
#
# if age >= 18:
#     print('You can Create Your EesyPassa Account💀')
# else:
#     print('You can\'t create your account😥')
#

# numer = random.randint(0, 1)
#
# if numer == 1:
#     print('Heads')


# -----------------------------------------------

# height = float(input('Enter Your Height in centimeter: '))
#
# if height >= 127:
#     print(f'You can take this ride😊 because your height is {height}cm')
# else:
#     print(f'You can\'t take this ride😥 because your height is {height}cm')

# drain_pipe = 3
#
# if drain_pipe >= 3:
#     print('Your water is Draining')
# else:
#     print('Enjoy!')


# BMI Calculator

# Get user input for weight and height
# weight = float(input("Enter your weight in kilograms: "))
# height = float(input("Enter your height in meters: "))
#
# # Calculate BMI
# bmi = weight / (height ** 2)
#
# # Display the BMI
# print(f"Your BMI is: {bmi:.2f}")
#
# # Determine the BMI category
# if bmi < 18.5:
#     print("You are underweight.")
# elif 18.5 <= bmi < 24.9:
#     print("You have a normal weight.")
# elif 25 <= bmi < 29.9:
#     print("You are overweight.")
# else:
#     print("You are obese.")


# ------------------------------------------------------------


height = float(input('Enter Your Height in centimeter: '))

bill = 0

if height >= 127:
    age = int(input('Enter Your age: '))
    if age >= 18:
        print(f'You can take this ride😊 because your height is {height}cm')
        bill += 12
        print(f'You have to give ${bill}')
    else:
        print(f'You can take this ride😊 because your height is {height}cm')
        bill += 8
        print(f'Your have to give ${8}')

    take_camera = input('Do you want to take a camera with you: (yes, no): ').capitalize()

    if take_camera == 'Yes':
        bill += 3
        print(f'Your Total Bill is ${bill}')


else:
    print(f'You can\'t take this ride😥 because your height is {height}cm')

