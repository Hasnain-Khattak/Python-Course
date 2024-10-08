import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card


user_cards = []
computer_cards = []
is_game_over = False

for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def calculate_score(cards):
    if len(cards) == 2 and 10 in cards and 11 in cards:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True

    else:
        want_another_card = input('Do you want to draw another card: (y or n): ').lower()
        if want_another_card == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

while computer_score != 0 or computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
    break

print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
# print(compare(user_score, computer_score))
