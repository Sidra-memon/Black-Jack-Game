import random
from replit import clear  # Ensure this is available
from Art import logo  # Ensure this is available

print(logo)

# Define the deck of cards
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(deck):
    """Returns a random card from the deck."""
    random.shuffle(deck)
    return deck.pop()

def calculate_score(cards):
    """Calculates the score of the given list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores and determines the winner."""
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

# Initialize the game
user_cards = []
computer_cards = []
is_game_over = False

# Deal initial two cards to each player
for _ in range(2):
    user_cards.append(deal_card(deck))
    computer_cards.append(deal_card(deck))

# Main game loop
while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    # Check for blackjack or bust
    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, 'n' to pass: ")
        if user_should_deal == 'y':
            user_cards.append(deal_card(deck))
        else:
            is_game_over = True

# Computer's turn to draw cards
while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card(deck))
    computer_score = calculate_score(computer_cards)

# Final scores and results
print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")

print(compare(user_score, computer_score))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()
