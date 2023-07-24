from typing import List, Dict
import random
import numpy as np
import sys
from BoardAnalyzer import compareHands
from Card import Card
from Player import Player
from PokerGame import PokerGame
from game_state import GameState

sb = 10
bb = 20

class Poker(GameState):
    #given a history determinen if the end game is reached
    #A round can only be over when you:
    #       check/fold after bet is made
    #       all in -> call
    #       call a bet after the river has appeared
    @staticmethod
    def is_terminal(game_state: PokerGame,history: str) -> bool:

        if(history[-2:] == "CC") and game_state.state=="RIVER":
            return True
        elif(history[-1]=="C") and (history[-2] not in ["*", "C"]):
            return True
        elif history[-1]=="K":
            if history[-2] == "A":
                return True
            elif game_state.state=="RIVER":
                return True

        return False

    #given the history, determine the payoff for player 1
    @staticmethod
    def get_payoff(history: str, board: List[Card], p1: List[Card], p2: List[Card], pot: int) -> int:
        result = compareHands(p1, p2, board)
        if result > 0:
            print("player 1 won!")
            return pot
        elif result < 0:
            print("player 2 won!")
            return -pot
        print("chop chop")
        return 0

    @staticmethod
    def get_handBucket(hand):
        return 0

    @staticmethod
    def get_actions():
        return ["A", "C", "K", "M", "T", "H", "P"]
        # A - represents all in
        # C - represents check/fold --> in the history if the previous the last action was c and the previous actions was not a * or c then the node is terminal
        # K - Call
        # M - Min bet
        # T - Bet 1/3 pot
        # H - Bet 1/2 pot
        # P - Bet Pot
        # * - represents chance node

    #returns if the current iteration of history is even valid
        #can be invalid in the following cases:
            #trying to min bet when another bet has already been placed
            #trying to bet more than a player has left
    @staticmethod
    def isValidHistory(history, action, playerStackSize, pot):
        match action:
            case"A":
                return True
            case "C":
                return True
            case "M":
                return history[-1] not in ["A", "K", "M", "T", "H", "P"]
            case "K":
                return history[-1] in ["A", "M", "T", "H", "P"]
            case "T":
                return (playerStackSize) >= int(pot/3)
            case "H":
                return (playerStackSize) >= int(pot/2)
            case "P":
                return (playerStackSize) >= pot
            case _:
                return False






