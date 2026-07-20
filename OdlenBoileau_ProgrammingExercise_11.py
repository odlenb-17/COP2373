# Import the Deck class

from deck import Deck

# Display the player's hand

def display_hand(hand):

    print("\nCurrent Hand")

    for i in range(len(hand)):

        print(i + 1, "-", hand[i])

# Replace selected cards

def replace_cards(deck, hand):

    choices = input(

        "\nEnter card numbers to replace (Example: 1 3 5): "

    )

    if choices == "":

        return

    numbers = choices.split()

    for number in numbers:

        if number.isdigit():

            position = int(number) - 1

            if 0 <= position < 5:

                hand[position] = deck.deal()

# Main program

def main():

    # Create a deck

    deck = Deck()

    # Store the player's cards

    hand = []

    # Deal five cards

    for i in range(5):

        hand.append(deck.deal())

    print("Initial Poker Hand")

    display_hand(hand)

    # Draw phase

    replace_cards(deck, hand)

    print("\nFinal Poker Hand")

    display_hand(hand)

# Run the program

main()
