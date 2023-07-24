def specify_actions():
    # A - represents all in
    # C - represents check/fold --> in the history if the previous the last action was c and the previous actions was not a * or c then the node is terminal
    # K - Call
    # M - Min bet
    # T - Bet 1/3 pot
    # H - Bet 1/2 pot
    # P - Bet Pot
    # * - represents chance node
    return ["C", "K", "M", "T", "H", "P", "A", "*"]
