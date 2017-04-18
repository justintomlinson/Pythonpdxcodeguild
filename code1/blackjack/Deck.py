import Card
import random

class Deck:
    def __init__ (self):
        """

        :param self:
        :return:
        """
        self.card_list = []


        for suit in Card.SUIT_NAME:
            for rank in Card.CARD_RANKS:
                cards = (rank + suit)
                self.card_list.append(cards)


    # def _eq_ (self):
    #     return

    def __repr__(self):
        if self.card_list == 0:
            return('no cards in the card_list')
        else:
            return


    def shuffle_deck(self):
        """

        :return:
        >>>
        """
        random.shuffle(self.card_list)
        return

    def draw_card_from_top(self):
        self.card_list.pop()
        return

def main():
    mydeck = Deck()
    print(repr(mydeck))


if __name__ == '__main__':
    main()