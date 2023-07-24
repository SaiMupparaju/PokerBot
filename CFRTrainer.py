from typing import List, Dict
import random

import BoardAnalyzer
import numpy as np
import sys

import ActionSpecifier
import hand_abstractor
from Card import Card
from Deck import Deck
from InformationSet import InformationSet
from Player import Player
from Poker import Poker
from PokerGame import PokerGame


Actions = ActionSpecifier.specify_actions()
bb = 20
sb = 10





# The CFRTrainer class is the class that uses the Poker class to run the train and CFR methods
class CFRTrainer():
    def __init__(self):
        self.infoset_map: Dict[str, InformationSet] = {} #Need to find a better way to represent
        self.cardsToBucketMapper = hand_abstractor.cardToBucketMapper(9)
    # Each decision node is defined uniquely by the card the player has and the current sequence of events,
    # we want to map each of these values to a unique infoSet

    #the palyerstate_and_history variable is a touple which stores p1s current hand tuple in the first element and game history str as second
    def get_information_set(self, playerstate_and_history) -> InformationSet:
        """add if needed and return"""
        if playerstate_and_history not in self.infoset_map:
            self.infoset_map[playerstate_and_history] = InformationSet()
        return self.infoset_map[playerstate_and_history]

    def getBucketGivenHand(self, playerHand: List[Card]):
        s = ""
        playerHand.sort(key= lambda x:x.rank)
        playerHand = playerHand[::-1]
        s += playerHand[0].getRank()
        s += playerHand[1].getRank()

        if playerHand[0].suit == playerHand[1].suit:
            s+="-S"
        else:
            s+="-O"
        return self.cardsToBucketMapper[s]

    # returns the cfr of the current node recursively
    def cfr(self, players: List[Player], history: str, reach_probabilities: np.array, active_idx: int, game_state: PokerGame, playerStacks: List[int], prevBet = 10):
        print(history)
        # base case: terminal node in which case
        if Poker.is_terminal(game_state, history):
            return Poker.get_payoff(
                history,
                game_state.board,
                players[active_idx].hand,
                players[1-active_idx].hand,
                game_state.pot)
        elif history[-1] == "K" or history[-2:] == "CC":
            game_state.next()
            players[0].strength = None
            players[1].strength = None


        board = game_state.board

        # We find the needed game values and info set by using HandBucket-handStrength-History as a key
        active_player = players[active_idx]
        active_cards = active_player.hand
        player_stack = playerStacks[active_idx]
        playerVal = str(self.getBucketGivenHand(active_cards)) + "-"
        if len(board) > 0:
            cards = board
            cards.append(active_cards)
            active_player.strength = active_player.strength if active_player.strength else BoardAnalyzer.AnalyzeHands(active_player, board)
            playerVal += str(active_player.strength) + "-"
            playerVal += "F" if BoardAnalyzer.checkFlushDraw(cards) else ""
            playerVal += "S" if BoardAnalyzer.checkStraightDraw(cards) else ""
        info_set = self.get_information_set(playerVal + "-" + history)
        curPot = game_state.pot



        strategy = info_set.get_strategy(reach_probabilities[active_idx])
        opp_idx = (active_idx + 1) % 2
        opp_player = players[opp_idx]
        opp_stack = playerStacks[opp_idx]

        # store the cf for each of the possible actions
        counterfactual_values = np.zeros(len(Actions))

        for ix, action in enumerate(Actions):
            if Poker.isValidHistory(history, action, player_stack, game_state.pot):
                action_probability = strategy[ix]

                # compute new reach probabilities after this action
                new_reach_probabilities = reach_probabilities.copy()
                new_reach_probabilities[active_idx] *= action_probability

                # recursively call cfr method, next player to act is the opp_player
                game_state.pot  += self.modifyPot(player_stack, action, curPot, prevBet)
                betMade = game_state.pot - curPot
                playerStacks[active_idx] -= betMade
                counterfactual_values[ix] = -self.cfr(
                    players=players,
                    history=history + action,
                    reach_probabilities=new_reach_probabilities,
                    active_idx=opp_idx,
                    game_state=game_state,
                    playerStacks=playerStacks,
                    prevBet=betMade)

                #reset the playerHands to what they were before
                playerStacks[active_idx] = player_stack
                playerStacks[opp_player] = opp_stack


        # calculate the new cfr with the new formula
        # Value of the current game state is just counterfactual values weighted by action probabilities
        node_value = counterfactual_values.dot(strategy)
        for ix, action in enumerate(Actions):
            info_set.cumulative_regrets[ix] += reach_probabilities[opp_idx] * (counterfactual_values[ix] - node_value)

        return node_value

    # simple set up
    def train(self, num_iterations: int) -> int:
        util = 0
        for i in range(num_iterations):
            print("round " + str(i+1))
            game_state = PokerGame(sb + bb)
            p1, p2 = game_state.p1, game_state.p2
            players = [p1, p2]
            player_stacks = [10000 - sb, 10000 - bb]
            history = '*'
            reach_probabilities = np.ones(2)
            util += self.cfr(players, history, reach_probabilities, 0, game_state, player_stacks, bb)
        print("util: " + str(util))
        return util



    # A - represents all in
    # C - represents check/fold --> in the history if the previous the last action was c and the previous actions was not a * or c then the node is terminal
    # K - Call
    # M - Min bet
    # T - Bet 1/3 pot
    # H - Bet 1/2 pot
    # P - Bet Pot
    # * - represents chance node, represetns the opening of the flop, turn, and river

    def modifyPot(self, playerStack: int, action: str, cur_pot: int, prevBet = 0):
        val = 0
        match (action):
            case 'A':
                val = playerStack
            case 'C':
                pass
            case 'K':
                val = prevBet if playerStack >= prevBet else playerStack
            case 'M':
                val = bb
            case 'T':
                val = int(cur_pot/3)
            case 'H':
                val = int(cur_pot/2)
            case _:
                val = cur_pot
        return val

trainer = CFRTrainer()
trainer.train(10)

