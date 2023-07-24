from abc import ABC, abstractmethod
from typing import List, Dict
import random
import numpy as np
import sys
from collections import Counter
from Player import Player
from Card import Card


def compareHands(p1: Player, p2: Player, board: List[Card]) -> int:
    p1Result = AnalyzeHands(p1, board)
    p2Result = AnalyzeHands(p2, board)
    # Check if p1 hand is better than p2
    if p1Result[0] < p2Result[0]:
        return 1
    elif p1Result[0] > p2Result[0]:
        return -1
    # If equal, then check values of the main hand
    elif (p1Result[0] == p2Result[0]) and (p1Result[1] > p2Result[1]):
        return 1
    elif (p1Result[0] == p2Result[0]) and (p1Result[1] < p2Result[1]):
        return -1
    # If we are dealing with a fullhouse or a t
    elif (p1Result[0] == p2Result[0]) and (p1Result[0] == 4):
        if p1Result[1] - p2Result[1] != 0:
            return p1Result[1] - p2Result[1]
        else:
            return p1Result[2] - p2Result[2] if (p1Result[2] - p2Result[2] != 0) else 0
    # If we are dealing with a two pair
    elif (p1Result[0] == p2Result[0]) and (p1Result[0] == 8):
        if p1Result[1] - p2Result[1] != 0:
            return p1Result[1] - p2Result[1]
        else:
            return p1Result[2] - p2Result[2] if (p1Result[2] - p2Result[2] != 0) else checkKickers(p1, p1Result, p2,
                                                                                                   p2Result, board, 1)
    else:
        match p1Result[0]:
            case 1:
                return 0
            case 2:
                return p1Result[1] - p2Result[1]
            case 3:
                if (p1Result[1] - p2Result[1] != 0):
                    return p1Result[1] - p2Result[1]
                return checkKickers(p1, p1Result, p2, p2Result, board, 1)
            case 7:
                if p1Result[1] - p2Result[1] != 0:
                    return p1Result[1] - p2Result[1]
                return checkKickers(p1, p1Result, p2, p2Result, board, 2)
            case 9:
                return p1Result[1] - p2Result[1] if ((p1Result[1] - p2Result[1]) != 0) else checkKickers(p1, p1Result,
                                                                                                         p2, p2Result,
                                                                                                         board, 3)
            case 10:
                return p1Result[1] - p2Result[1] if ((p1Result[1] - p2Result[1]) != 0) else checkKickers(p1, p1Result,
                                                                                                         p2,
                                                                                                         p2Result,
                                                                                                         board, 4)
            case _:
                return p1Result[1] - p2Result[1]


def checkKickers(p1: Player, p1Result, p2: Player, p2Result, board, numKickers):
    # Rankings are the same, check kickers
    # Gather all the cards
    cards1 = [card for card in board]
    cards1.extend(p1.hand)
    cards2 = [card for card in board]
    cards2.extend(p2.hand)

    # Sort the cards by rank
    cards1 = sorted(cards1, key=lambda card: card.rank, reverse=True)
    cards2 = sorted(cards2, key=lambda card: card.rank, reverse=True)

    # Remove cards that are part of the main hand
    for card in p1Result[1:]:
        cards1 = [card for card in cards1 if card.rank != card]
    for card in p2Result[1:]:
        cards2 = [card for card in cards2 if card.rank != card]

    # Compare the kickers
    for i in range(numKickers):
        if cards1[i].rank > cards2[i].rank:
            return p1
        elif cards1[i].rank < cards2[i].rank:
            return p2
    return 0


def AnalyzeHands(player: Player, board: List[Card]) -> List[int]:
    # initialize the cards array
    cards = [card for card in board]
    cards.append(player.hand[0])
    cards.append(player.hand[1])
    # Next we just go through all significant poker hands to see if we have something
    # We return the overall hand ranking of whatever we have:
    # Check royal,straight flushes
    hasStraightFlush = checkStraightFlush(cards)
    if hasStraightFlush[0]:
        if hasStraightFlush[1] == 14:
            return (1, None)
        else:
            return (2, hasStraightFlush[1])
    # check Quads
    hasQuads = checkQuads(cards)
    if hasQuads[0]:
        return (3, hasQuads[1])
    # check full house
    hasFull = checkFullHouse(cards)
    if hasFull[0]:
        return (4, hasFull[1], hasFull[2])
    # check flush
    hasFlush = checkFlush(cards)
    if hasFlush[0]:
        return (5, hasFlush[1])
    # check Straight
    hasStraight = checkStraight(cards)
    if hasStraight[0]:
        return (6, hasStraight[1])
    # check set
    hasSet = checkSet(cards)
    if hasSet[0]:
        return (7, hasSet[1])
    # check Two Pair
    hasTwoPair = checkTwoPair(cards)
    if hasTwoPair[0]:
        return (8, hasTwoPair[1], hasTwoPair[2])
    # check Pair
    hasPair = checkPair(cards)
    if hasPair[0]:
        return (9, hasPair[1])
    # If has nothing else, return high card.
    return (10, max([card.rank for card in cards]))


def checkFlush(boardStr):
    suits = {'H': 0, 'C': 0, 'S': 0, 'D': 0}
    highestRankPerSuit = {'H': 0, 'C': 0, 'S': 0, 'D': 0}
    for card in cards:
        suits[card.suit] += 1
        if card.rank > highestRankPerSuit[card.suit]:
            highestRankPerSuit[card.suit] = card.rank
    for suit in suits:
        if suits[suit] >= 5:
            return (True, highestRankPerSuit[suit])
    return (False, None)


def checkStraight(cards):
    # Create a set of ranks to handle duplicates and sort them
    sorted_ranks = sorted({card.rank for card in cards})

    # Check if we have a straight with Ace as 1 (this would mean we have a 2 in our hand)
    if 14 in sorted_ranks and sorted_ranks[0:4] == list(range(2, 6)):
        return (True, 5)

    # Check for regular straights
    for i in range(len(sorted_ranks) - 4, -1, -1):
        # If these five cards make a straight
        if sorted_ranks[i:i + 5] == list(range(sorted_ranks[i], sorted_ranks[i] + 5)):
            return (True, sorted_ranks[i] + 4)
    return (False, None)


def checkStraightFlush(cards: List[Card]):
    # Group cards by suit and check each suit separately
    suits = {'HEART': [], 'CLUB': [], 'SPADE': [], 'DIAMOND': []}
    for card in cards:
        suits[card.suit].append(card)

    for suit in suits:
        ans = checkStraight(suits[suit])
        if ans:
            return (True, ans[1])

    return (False, None)


def checkQuads(cards):
    ranks = {}
    for card in cards:
        if card.rank in ranks:
            ranks[card.rank] += 1
        else:
            ranks[card.rank] = 1
    for rank in ranks:
        if ranks[rank] == 4:
            return (True, rank)
    return (False, None)


def checkFullHouse(cards):
    # Count the occurrence of each rank
    # Count the occurrence of each rank
    ranks = [card.rank for card in cards]
    rank_counts = Counter(ranks)

    # Get the ranks that appear three times and two times
    threes = [rank for rank, count in rank_counts.items() if count == 3]
    twos = [rank for rank, count in rank_counts.items() if ((count >= 2) and (count < 4))]

    # If there's no three-of-a-kind, there's no full house
    if len(threes) == 0:
        return (False, None, None)

    # If there's no pair (aside from the three-of-a-kind), there's no full house
    if len(twos) == 0:
        return (False, None, None)

    # Get the highest three-of-a-kind and the second highest pair (which could also be a three-of-a-kind)
    top_three = max(threes)
    twosWithoutTopThree = [rank for rank in twos if rank != top_three]
    if len(twosWithoutTopThree) == 0:
        return (False, None, None)
    top_two = max(twosWithoutTopThree)

    return (True, top_three, top_two)


def checkSet(cards):
    ranks = {}
    for card in cards:
        if card.rank in ranks:
            ranks[card.rank] += 1
        else:
            ranks[card.rank] = 1
    hasSet = False
    highestRankedSet = 0
    for rank in ranks:
        if ranks[rank] == 3:
            hasSet = True
            if rank > highestRankedSet:
                highestRankedSet = rank
    if hasSet:
        return (True, highestRankedSet)
    return (False, None)


def checkPair(cards):
    # Count the occurrence of each rank
    ranks = [card.rank for card in cards]
    rank_counts = Counter(ranks)

    # Get the ranks that appear two or more times
    pairs = [rank for rank, count in rank_counts.items() if count >= 2]

    # If there's no pair, return (False, None)
    if not pairs:
        return (False, None)

    # Get the highest pair
    top_pair = max(pairs)

    return (True, top_pair)


def checkTwoPair(cards):
    # Count the occurrence of each rank
    ranks = [card.rank for card in cards]
    rank_counts = Counter(ranks)

    # Get the ranks that appear two or more times
    pairs = [rank for rank, count in rank_counts.items() if count >= 2]

    # If there are less than two pairs, return (False, None, None)
    if len(pairs) < 2:
        return (False, None, None)

    # Sort the pairs and get the top two
    top_pairs = sorted(pairs, reverse=True)[:2]

    return (True, top_pairs[0], top_pairs[1])


def checkFlushDraw(cards):
    # Count the occurrences of each suit
    suits = [card.suit for card in cards]
    suit_counts = Counter(suits)

    # Check if any suit count is 4 (indicating a flush draw)
    for count in suit_counts.values():
        if count == 4:
            return True
    return False


def checkStraightDraw(cards):
    ranks = {card.rank for card in cards}
    ranks = sorted([rank for rank in ranks])
    for i in range(0, len(ranks) - 3):
        if ranks[i:i + 4] == [ranks[i] + j for j in range(4)]:
            return True
    return False

# cards = [Card(2, "H"), Card(3, "D"), Card(4, "S"), Card(5, "C"), Card(13, "D"), Card(13, "C"), Card(13, "D")]
# print(" Straight flush")
# print(checkStraightFlush(cards))
# print("--------------------- \n Straight")
# print(checkStraight(cards))
# print("--------------------- \n Flush")
# print(checkFlush(cards))
# print("--------------------- \n Full House")
# print(checkFullHouse(cards))
# print("--------------------- \n Quads")
# print(checkQuads(cards))
# print("--------------------- \n Set")
# print(checkSet(cards))
# print("--------------------- \n Two Pair")
# print(checkTwoPair(cards))
# print("--------------------- \n Pair")
# print(checkPair(cards))
# print("--------------------- \n Flush Draw")
# print(checkFlushDraw(cards))
# print("--------------------- \n Straight Draw")
# print(checkStraightDraw(cards))
