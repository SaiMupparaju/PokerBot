from Card import Card
import numpy as np

class Deck:
    def __init__(self):
        self.deck = []
        for suit in ["SPADE", "CLUB", "HEART", "DIAMOND"]:
            for rank in range(2, 15):
                self.deck.append(Card(rank, suit))
        self.deck = np.array(self.deck)
        self.pointer = 0

    def shuffle(self):
        np.random.shuffle(self.deck)

    def dealNext(self):
        if self.pointer > len(self.deck) - 1:
            return None
        else:
            c = self.deck[self.pointer]
            self.pointer = self.pointer + 1
            return c

