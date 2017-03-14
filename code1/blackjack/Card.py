SUIT_NAME = ['c', 'd', 'h', 's']
CARD_RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:

    def __init__ (self, SUIT_NAME, CARD_RANKS):
        self.suit = SUIT_NAME
        self.rank = CARD_RANKS

    # def _eq_ (self):
    #     return

    def __repr__(self):
        return(self.rank + self.suit)


def main():
    mycard = Card(SUIT_NAME[0], CARD_RANKS[0])
    mysuit = mycard.suit
    myrank = mycard.rank
    print(repr(mycard))
if __name__ == '__main__':
    main()