from blackjack_art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(hand):
    score = sum(hand)

    if score == 21 and len(hand) == 2:
        return 0
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    return score

def compare(u_score , c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def game():
    user_cards = []
    computer_cards = []
    user_score = -1
    computer_score = -1


    print(logo)

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    playing = True

    while playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            playing = False
        else:
            want_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if want_card == "y":
                user_cards.append(deal_card())
            else:
                playing = False

    while computer_score!=0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    print(compare(user_score , computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
    print("\n" * 50)
    game()