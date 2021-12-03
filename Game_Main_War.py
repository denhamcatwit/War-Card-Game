import Card  # Card Class


class Game_Main_War():
    # Initial Constructor Class
    def __init__(self):
        self.player_list = []
        Game_Main_War.game_start(self)  # Calls Game Loop

    def get_players(self):  # Gets the players from server then passes them
        pass

    def isWar(self, player1, player2, card_num):  # Checks if the players are going to have an Active War
        value1 = Card.Card.val(player1[card_num])
        value2 = Card.Card.val(player2[card_num])
        if value1 != value2:
            return False
        else:
            return game_main.activeWar(self, player1, player2,
                                       card_num)  # If Players have Active War, then calls ActiveWar method

    def deckHandling(self, playerW, playerL, card_num, winner):  # Handles deck based off winner or loser
        if winner:
            playerW.append(playerW[card_num])
            playerW.append(playerL[card_num])
            playerW.remove(playerW[card_num])
            return playerW
        else:
            playerL.remove(playerW[card_num])
            return playerL

    def activeWar(self, player1, player2, card_num):  # If isWar is true, then War is initiated
        global SDeck
        card_num += 4
        Card1 = player1[card_num]
        Card2 = player2[card_num]
        if Card.Card.val(Card1) > Card.Card.val(Card2):  # Checks if after War, who is the winner
            for count in card_num:
                tempDeck = game_main.deckHandling(self, player1, player2, card_num, True)
                tempDeck2 = game_main.deckHandling(self, player1, player2, card_num, False)
                SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck
        elif Card.Card.val(Card1) < Card.Card.val(Card2):  # Checks if after War, who is the winner
            for count in card_num:
                tempDeck = game_main.deckHandling(self, player2, player1, card_num, True)
                tempDeck2 = game_main.deckHandling(self, player2, player1, card_num, False)
                SDeck = Card.DeckOfDecks.add(SDeck, tempDeck, tempDeck2)
            return SDeck
        else:
            return self.activeWar(player1, player2, card_num)  # Recursion if the War continues, calls itself back

    def playerWon(self, player1, player2, x):  # If isWar is false, then this method is called to determine the Winner
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

    def game_start(self):  # Game Loop
        # game_main.player_list.append(player_from_server)
        game_Active: bool = True
        game_deck.shuffle()
        player1 = game_deck.deal(game_deck, 0)
        player2 = game_deck.deal(game_deck, 1)
        global super_deck

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
