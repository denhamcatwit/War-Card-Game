import random


class Card(object):
    suits = ['D', 'H', 'S', 'C']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    value = 0
    suit = ''

    def __init__(self, value, suit):  # Initializes it for each card when called
        self.value = value
        self.suit = suit

    def val(self):  # Returns value
        return self.value

    def suit(self):  # Returns suit
        return self.suit


class Deck(object):  # Holds Multiple Cards
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(Card.values[value], Card.suits[suit]) # Goes through the entire lists assigning each card
                # to initial deck
                self.deck.append(card)
        random.shuffle(self.deck)

    def shuffle(self):  # Shuffles using Random
        random.shuffle(self.deck)

    def deal(self, FullDeck, num):  # Deals Cards
        if num == 0:
            return FullDeck[:len(FullDeck) // 2]
        if num == 1:
            return FullDeck[len(FullDeck) // 2:]

    def reset(self):  # Resets deck
        while len(self.deck) > 0:
            self.deck.pop()


class DeckOfDecks(object):  # Holds multiple Decks to pass
    def __init__(self):
        self.super_deck = []

    def add(self, Deck1, Deck2):  # Clears itself, then adds new Decks
        self.super_deck.clear()
        self.super_deck.append(Deck1)
        self.super_deck.append(Deck2)

    def clear(self):
        self.super_deck.pop()
        self.super_deck.pop()
