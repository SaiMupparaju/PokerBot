from Deck import Deck
from Player import Player



class PokerGame():
    def __init__(self):
        self.deck = Deck()
        self.p1, self.p2 = self.init_hands(self.deck)
        self.state = "PREFLOP"
        self.board = []
        self.pot = 0
        self.history = ""

    def __init__(self, _pot):
        self.deck = Deck()
        self.p1, self.p2 = self.init_hands(self.deck)
        self.state = "PREFLOP"
        self.board = []
        self.pot = _pot


    def next(self):
        match (self.state):
            case "PREFLOP":
                self.board  = [self.deck.dealNext() for i in range(3)]
                self.state = "FLOP"
            case "FLOP":
                self.board.append(self.deck.dealNext())
                self.state = "TURN"
            case "TURN":
                self.board.append(self.deck.dealNext())
                self.state = "RIVER"
            case _:
                pass
        return self.board

    def init_hands(self, game_deck: Deck):
        p1 = Player()
        p1Hand = [game_deck.dealNext()]
        p1Hand.append(game_deck.dealNext())
        p1.hand = p1Hand
        p2 = Player()
        p2Hand = [game_deck.dealNext()]
        p2Hand.append(game_deck.dealNext())
        p2.hand = p2Hand
        return p1, p2




