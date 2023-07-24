from Deck import Deck
from Card import Card
gameHistory = []
curCard = Card("HEART", 14)


def getGuess(curCard, history, cardsLeft):
    p = getChanceBelow(curCard.rank, history, cardsLeft)
    if p > 0.5:
        return "BELOW"
    return "ABOVE"


def getChanceBelow(rank, history, cardsLeft):
    s = 0
    for i in range(2, rank):
        s += history[i]
    return (1.0 * s) / cardsLeft

for i in range(1, 1000001):
    print(i)
    deck = Deck()
    deck.shuffle()
    curRun = 1
    curCard = deck.dealNext()
    history = {}
    cardLeft = 51
    for i in range(2, 15):
        history[i] = 13
    history[curCard.rank] = history[curCard.rank] - 1
    guess = getGuess(curCard, history, cardLeft)
    while cardLeft > 0:
        nextCard = deck.dealNext()
        cardLeft += -1
        if nextCard:
            if guess == "ABOVE":
                if nextCard.rank >= curCard.rank:
                    curRun += 1
                else:
                    gameHistory.append(curRun)
                    curRun = 1
                    print("-----")
                    break
            else:
                if nextCard.rank <= curCard.rank:
                    curRun+=1
                else:
                    gameHistory.append(curRun)
                    curRun = 1
                    print("-----")
                    break

        curCard = nextCard
        history[curCard.rank] = history[curCard.rank] - 1
        guess = getGuess(curCard, history, cardLeft)

    average = (1.0 * sum(gameHistory))/len(gameHistory)
    print("Average run size: " +  str(average))


