import art
import random

def start_or_end():
    """Starts or ends the program according to user input"""
    s = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    return s
def deal(cards, number_of_cards):
    """Deals random cards according to the number of cards the user asks"""
    list = [0] * number_of_cards
    for n in range(number_of_cards):
        list[n] = random.choice(cards)
    return list
def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21  and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

start = start_or_end()
while start == "y":
    if start == "y":
        print(art.logo)


    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    Users_card = deal(cards,2)
    Computers_card = deal(cards,2)
    User_score = calculate_score(Users_card)
    Computer_score = calculate_score(Computers_card)

    print(f"Your cards: {Users_card}", " ", end="")
    print(f"Current Score: {User_score}")
    print(f"Computer's first card: {Computers_card[0]}")
    if User_score == 0:
        print("You win with a BlackJack 😎")
        start = start_or_end()
        continue
    elif Computer_score == 0:
        print("You lose. Computer has a BlackJack 😱")
        start = start_or_end()
        continue
    continuation = True
    while continuation:
        should_continue = input("Type 'y' to get another card,type 'n' to pass: ")
        if should_continue == 'y':
            Users_card.append(deal(cards, 1)[0])
            User_score = calculate_score(Users_card)
            if User_score > 21:
                print(f"Your final hand: {Users_card}", " ", end="")
                print(f"Final Score: {User_score}")
                print(f"Computer's final hand: {Computers_card}"," ", end="")
                print(f"Final Score: {Computer_score}")
                print("You went over you lose 😭")
                start = start_or_end()
                continuation = False
                break
            Computers_choice = random.choice([True, False])
            if Computers_choice:
                Computers_card.append(deal(cards, 1)[0])
                Computer_score = calculate_score(Computers_card)
            if Computer_score > 21:
                print(f"Your final hand: {Users_card}", " ", end="")
                print(f"Final Score: {User_score}")
                print(f"Computer's final hand: {Computers_card}", " ", end="")
                print(f"Final Score: {Computer_score}")
                print("Opponent went over You WIN! 🥳")
                start = start_or_end()
                continuation = False
                break
            print(f"Your cards: {Users_card}", " ", end="")
            print(f"Current Score: {User_score}")
            print(f"Computer's first card: {Computers_card[0]}")
            continuation = True
        else:
            Computers_choice = random.choice([True, False])
            if Computers_choice == True:
                Computers_card.append(deal(cards, 1)[0])
                Computer_score = calculate_score(Computers_card)
            if Computer_score > 21:
                print(f"Your final hand: {Users_card}", " ", end="")
                print(f"Final Score: {User_score}")
                print(f"Computer's final hand: {Computers_card}", " ", end="")
                print(f"Final Score: {Computer_score}")
                print("Opponent went over You WIN! 🥳")
                start = start_or_end()
                continuation = False
                break
            print(f"Your final hand: {Users_card}", " ", end="")
            print(f"Final Score: {User_score}")
            print(f"Computer's final hand: {Computers_card}", " ", end="")
            print(f"Final Score: {Computer_score}")
            if User_score == Computer_score:
                print("Draw")
            elif User_score > Computer_score:
                print("You WIN!🥳")
            else:
                print("You Lose😭")
            continuation = False
            start = start_or_end()