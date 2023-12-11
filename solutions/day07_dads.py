from typing import Union, List


def get_input(filepath: str, split="\n") -> Union[List[str], str]:
    with open(filepath, "r") as fp:
        string = fp.read()
    if not split:
        return string
    return string.split(split)


class Hand:
    CheckString = "AKQJT98765432"

    def __repr__(self) -> str:
        return f"Hand({self.Cards, self.TypeWeight, self.CardRanks})"

    def __init__(self):
        self._Data = ""
        self.Cards = ""
        self.CardRanks = []
        self.BidAmount = 0
        self.Cardvals = ""
        self.TypeOfHand = ""
        self.TypeWeight = 0
        self.Rank = 0

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, value):
        self._Data = value
        self.Cards = self._Data.split(" ")[0]
        self.BidAmount = int(self._Data.split(" ")[1])
        self.RankCards()
        self.Entropy()

    def RankCards(self):
        for i in range(5):
            self.CardRanks.append(
                list(reversed(self.CheckString)).index(self.Cards[i])
            )  # CHANGED TO REVERSED

    def HandType(self):
        if "5" in self.Cardvals:
            self.TypeOfHand = "Five of a    kind"
            self.TypeWeight = 6
        elif "4" in self.Cardvals:
            self.TypeOfHand = "Four of a kind"
            self.TypeWeight = 5
        elif "3" in self.Cardvals:
            if "2" in self.Cardvals:
                self.TypeOfHand = "Full House"
                self.TypeWeight = 4
            else:
                self.TypeOfHand = "Three of a kind"
                self.TypeWeight = 3
        else:
            card_counts = self.Cardvals.split("2")
            if len(card_counts) == 3:
                self.TypeOfHand = "Two Pair"
                self.TypeWeight = 2
            elif len(card_counts) == 2:
                self.TypeOfHand = "One Pair"
                self.TypeWeight = 1
            else:
                self.TypeOfHand = "High Card"
                self.TypeWeight = 0

    def Entropy(self):
        self.Cardvals = ""
        for a in self.CheckString:
            self.Cardvals += str(self.Cards.count(a))
        self.HandType()


def Day7(mydata):
    hands = []
    for m in mydata:
        h = Hand()
        h.Data = m
        hands.append(h)
    hands.sort(key=lambda x: (x.TypeWeight, [x.CardRanks[i] for i in range(4)]))

    total = 0
    for i in range(len(hands)):
        hands[i].Rank = i + 1
        total += hands[i].Rank * hands[i].BidAmount

    return total


if __name__ == "__main__":
    for file, expected in [
        ("solutions/example_inputs/07", 6440),
        ("solutions/inputs/07", 246912307),
    ]:
        print(file)
        ans = Day7(get_input(file))
        print(ans, expected)
        print(ans == expected)
