class Card:


    def __init__(self, cardRank: int, cardSuite: str):
        self.rank = cardRank
        self.suit = cardSuite

    def __main__(self):
        pass

    def __str__(self):
        ans = ""
        if self.rank >= 2 and self.rank < 10:
            ans+= str(self.rank)
        else:
            match self.rank:
                case 1:
                    ans+= "A"
                case 10:
                    ans+= "T"
                case 11:
                    ans+= "J"
                case 12:
                    ans+= "Q"
                case _:
                    ans+= "K"
        match self.suit:
            case "SPADE":
                ans += "S"
            case "CLUB":
                ans += "C"
            case "HEART":
                ans += "H"
            case _:
                ans += "D"

        return ans

    def getRank(self):
        if self.rank>=2 and self.rank < 10:
            return str(self.rank)
        else:
            match self.rank:
                case 1:
                    return "A"
                case 10:
                    return "T"
                case 11:
                    return "J"
                case 12:
                    return "Q"
                case _:
                    return "K"
