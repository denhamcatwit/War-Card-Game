import random
import MergeSort


class Card(object):
    suits = ['D', 'H', 'S', 'C']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    value = 0
    suit: str = ''

    def __init__(self, value: int, suit: str):  # Initializes it for each card when called
        self.value = value
        self.suit = suit

    def get_value(self):  # Returns value
        return self.value

    def get_suit(self):  # Returns suit
        return self.suit


class Deck(object):  # Holds Multiple Cards
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)  # Goes through the entire lists assigning each card
                # to initial deck
                self.deck.append(card)
        temp = MergeSort.MergeSort.__init__(self)
        random.shuffle(self.deck)
        self.deck = MergeSort.MergeSort.merge_sort_(temp, self.deck, len(self.deck))
        random.shuffle(self.deck)

    def deal(self, full_deck, num):  # Deals Cards
        if num == 0:
            return full_deck[:len(full_deck) // 2]
        if num == 1:
            return full_deck[len(full_deck) // 2:]

    def reset(self):  # Resets deck
        while len(self.deck) > 0:
            self.deck.pop()


class DeckOfDecks(object):  # Holds multiple Decks to pass
    def __init__(self):
        self.super_deck = []

    def add(self, deck1, deck2):  # Clears itself, then adds new Decks
        self.super_deck.pop()
        self.super_deck.pop()
        self.super_deck.append(deck1)
        self.super_deck.append(deck2)
