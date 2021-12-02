import Card #


class Game_Main_War():
    def __init__(self):
        self.cards_on_table = []
        self.player_list = []

        Game_Main_War.game_start(self)

        #def round_start(self):
        #for player in self.player_list:
        #   self.round_list.append(player)

    def get_players(self):
        pass

    def deal(self):
        for player in self.player_list:
            player.hand = game_deck.deal(self, player)

    def isWar(self, player1, player2, x):
        value1 = Card.Card.val(player1[x])
        value2 = Card.Card.val(player2[x])
        if value1 != value2:
            return False
        else:
            return game_main.activeWar(self, player1, player2, x)

    def deckHandling(self, playerW, playerL, x, test):
        if test == True:
            playerW.append(playerW[x])
            playerW.append(playerL[x])
            playerW.remove(playerW[x])
            return playerW
        else:
            playerL.remove(playerW[x])
            return playerL

    def activeWar(self, player1, player2, x):
        global SDeck
        x += 4
        Card1 = player1[x]
        Card2 = player2[x]
        if Card.Card.val(Card1) > Card.Card.val(Card2):
            for count in x:
                tempDeck = game_main.deckHandling(self, player1, player2, x, True)
                tempDeck2 = game_main.deckHandling(self, player1, player2, x, False)
                SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck
        elif Card.Card.val(Card1) < Card.Card.val(Card2):
            for count in x:
                tempDeck = game_main.deckHandling(self, player2, player1, x, True)
                tempDeck2 = game_main.deckHandling(self, player2, player1, x, False)
                SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck
        else:
            return self.activeWar(player1, player2, x)  # Recursion

    def playerWon(self, player1, player2, x):
        global SDeck
        if Card.Card.val(player1) > Card.Card.val(player2):
            tempDeck = game_main.deckHandling(self, player1, player2, x, True)
            tempDeck2 = game_main.deckHandling(self, player1, player2, x, False)
            SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck
        else:
            tempDeck = game_main.deckHandling(self, player2, player1, x, True)
            tempDeck2 = game_main.deckHandling(self, player2, player1, x, False)
            SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck

    def game_start(self):
        #game_main.player_list.append(player_from_server)
        game_Active: bool = True
        game_deck.shuffle()
        player1 = game_deck.deal(game_deck, 0)
        player2 = game_deck.deal(game_deck, 1)

        # game_deck = Card

        # game_main.deal_players()
        while game_Active:
            num = 0
            player1C = player1[num]
            player2C = player2[num]
            isWar = game_main.isWar(self, player1C, player2C, num)
            global SDeck
            if not isWar:
                SDeck = game_main.isWar(self, player1C, player2C, num)


game_main = Game_Main_War
game_main.player_list = []
game_deck = Card.Deck()
