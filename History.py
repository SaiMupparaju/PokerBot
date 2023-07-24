#helper function, we can use it when iterating through actions to determine if an action is valid in the current context


# A - represents all in
# C - represents check/fold --> in the history if the previous the last action was c and the previous actions was not a * or c then the node is terminal
# K - Call
# M - Min bet
# T - Bet 1/3 pot
# H - Bet 1/2 pot
# P - Bet Pot
# * - represents chance node

invalidOrders = ["*K", "AT", "AH", "AP", "AM"]


def valid_order(history: str):
    return not(history[-2:] in invalidOrders)
