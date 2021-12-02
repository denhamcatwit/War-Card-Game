import random


class Card(object):
    suits = ['D', 'H', 'S', 'C']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    value = 0
    suit = ''

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def val(self):
        return self.value

    def suit(self):
        return self.suit


class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(Card.values[value], Card.suits[suit])
                self.deck.append(card)
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, FullDeck, num):
        if num == 0:
            return FullDeck[:len(FullDeck) // 2]
        if num == 1:
            return FullDeck[len(FullDeck) // 2:]

    def reset(self):
        while (len(self.deck) > 0):
            self.deck.pop()


class DeckOfDecks(object):
    def __init__(self):
        self.ddeck = []

    def add(self, Deck1, Deck2):
        self.ddeck.pop()
        self.ddeck.pop()
        self.ddeck.append(Deck1)
        self.ddeck.append(Deck2)
