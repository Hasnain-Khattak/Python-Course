import random
import achi

word_list = ["apple", "mango", "orange"]

choose_word = random.choice(word_list)
word_length = len(choose_word)

display = []


for _ in range(word_length):
    display += '_'

lives = 6

game_on = True

while game_on:
    guess = input("Enter any letter: ").lower()
    for position in range(word_length):
        letter = choose_word[position]
        if guess == letter:
            display[position] = letter
    if guess not in choose_word:
        lives -= 1
        if lives == 0:
            game_on = False
            print("You lose.")
    print(f"{' '.join(display)}")
    print('Remaining Lives {}'.format(lives))

    if '_' not in display:
        print('You win')
        game_on = False
    print(achi.stages[lives])
