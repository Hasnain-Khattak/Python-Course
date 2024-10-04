try:
    score = int(input('Enter Your score: '))
    if score > 60:
        print('Pass')
except ValueError:
    print('Please enter a valid integer.')