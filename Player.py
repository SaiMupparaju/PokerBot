from abc import ABC, abstractmethod
from typing import List, Dict
import random
import numpy as np
import sys
from Card import Card

class Player:
    def __init__(self):
        self.hand = []
        self.stack = 0
        #this is a more abstract value that is used during training, easiest to keep track of here
        self.strength = None

    def add_startingHand(self, card1: Card, card2: Card):
        self.hand.append(card1)
        self.hand.append(card2)

    def initStack(self, amount: int):
        self.stack = amount

    def bet(self, bet: int):
        self.stack = max([0, self.stack - bet])

    def __str__(self):
        if self.hand is None:
            return ""
        return str(self.hand[0])+str(self.hand[1])
    