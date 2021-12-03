import random


class Card(object):
    suits = ['D', 'H', 'S', 'C']
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    value = 0
    suit: str = ''

    def __init__(self, value: int, suit: str):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class Deck(object):
    def __init__(self):
        self.deck = []
        for suit in Card.suits:
            for value in Card.values:
                card = Card(value, suit)
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
        self.super_deck = []

    def add(self, Deck1, Deck2):
        self.super_deck.pop()
        self.super_deck.pop()
        self.super_deck.append(Deck1)
        self.super_deck.append(Deck2)
