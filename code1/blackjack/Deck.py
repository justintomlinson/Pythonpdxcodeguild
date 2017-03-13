import Card
import random

class Deck:
    def _init_ (self):
        """

        :param self:
        :return:
        """
        self.deck = []
        self.suit = Card.Card(suit)
        self.rank = Card.Card(rank)

        for suit in Card.SUIT_NAME:
            for rank in Card.CARD_RANKS:
                cards = (suit, rank)
                self.deck.append(cards)


    def _eq_ (self):
        return

    def _repr_(self):

        return

    def shuffle_deck(self):
        random.shuffle(self.deck)
        return

    def draw_card_from_top(self):
        #
        return

    def main(x):
    #if running this module directly do x else do nothing
    if __name__ == '__main__':
        main()