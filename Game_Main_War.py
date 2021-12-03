import Card
from game import Game

class Game_Main_War():

    def __init__(self):
        self.player_list = []
        Game_Main_War.game_start(self)



# Need fxn to assign the two players in each table to player1[], player2[]
    # They are lists that hold cards.
    #
    # Not Sure how to do that
    #
    #
    ###################

    def get_players(self):
        pass

# Fills player lists with cards they are assigned.
    def deal(self):
        for player in self.player_list:
            player.hand = game_deck.deal(self, player)

# Optional boolean that checks if cards are not a match, if they are a match, calls activeWar
    def isWar(self, player1, player2, card_num):
        value1 = Card.Card.get_value(player1[card_num])
        value2 = Card.Card.get_value(player2[card_num])
        if value1 != value2:
            return False
        else:
            return game_main.activeWar(self, player1, player2, card_num)

# Gives the Winner the losers card, removes card from losers pile
    def deckHandling(self, playerW, playerL, card_num, test):
        if test == True:
            playerW.append(playerW[card_num])
            playerW.append(playerL[card_num])
            playerW.remove(playerW[card_num])
            return playerW
        else:
            playerL.remove(playerW[card_num])
            return playerL

# Like in the card game, activeWar wagers 3 cards and compares the 4th to find winner of total card pot
    def activeWar(self, player1, player2, card_num):
        global super_deck
        card_num += 4
        Card1 = player1[card_num]
        Card2 = player2[card_num]
        if Card.Card.get_value(Card1) > Card.Card.get_value(Card2):
            for count in card_num:
                tempDeck = game_main.deckHandling(self, player1, player2, card_num, True)
                tempDeck2 = game_main.deckHandling(self, player1, player2, card_num, False)
                super_deck = Card.DeckOfDecks.add(super_deck, tempDeck, tempDeck2)
            return super_deck
        elif Card.Card.get_value(Card1) < Card.Card.get_value(Card2):
            for count in card_num:
                tempDeck = game_main.deckHandling(self, player2, player1, card_num, True)
                tempDeck2 = game_main.deckHandling(self, player2, player1, card_num, False)
                super_deck = Card.DeckOfDecks.add(super_deck, tempDeck, tempDeck2)
            return super_deck
        else:
            return self.activeWar(player1, player2, card_num)  # Recursion

# Determines which card is of higher value, assigns winner to owner of higher valued card.
    def playerWon(self, player1, player2, card_num):
        global super_deck
        if Card.Card.get_value(player1) > Card.Card.get_value(player2):
            tempDeck = game_main.deckHandling(self, player1, player2, card_num, True)
            tempDeck2 = game_main.deckHandling(self, player1, player2, card_num, False)
            super_deck = Card.DeckOfDecks.add(super_deck, tempDeck, tempDeck2)
            return super_deck
        else:
            tempDeck = game_main.deckHandling(self, player2, player1, card_num, True)
            tempDeck2 = game_main.deckHandling(self, player2, player1, card_num, False)
            super_deck = Card.DeckOfDecks.add(super_deck, tempDeck, tempDeck2)
            return super_deck

# Begins the game, deals the player-hands.
    def game_start(self):
        #game_main.player_list.append(player_from_server)
        game_Active: bool = True
        game_deck.shuffle()
        player1 = game_deck.deal(game_deck, 0)
        player2 = game_deck.deal(game_deck, 1)
        global super_deck
        # game_deck = Card

        # game_main.deal_players()
        while game_Active:
            card_num = 0
            is_war = game_main.isWar(self, player1, player2, card_num)
            if not is_war:
                super_deck = game_main.isWar(self, player1, player2, card_num)
            else:
                super_deck = is_war
            player1 = super_deck[0]
            player2 = super_deck[1]



game_main = Game_Main_War
game_main.player_list = []
game_deck = Card.Deck()
