# deck.py

import random

class Deck:

    # Constructor

    def __init__(self):

        self.cards = []

        # Create a deck of 52 cards

        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

        ranks = ["Ace", "2", "3", "4", "5", "6", "7",

                 "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:

            for rank in ranks:

                self.cards.append(rank + " of " + suit)

        random.shuffle(self.cards)

    # Deal one card

    def deal(self):

        return self.cards.pop()
