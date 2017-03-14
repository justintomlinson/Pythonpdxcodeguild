"""This module creates and scores a hand of blackjack. It will alert the user if they are over 21 """
import Deck
import Card


class Hand:
    def __init__ (self):
        """ Establish hand with 2 cards

        :return:
        """
        self.deck = Deck.Deck()
        self.hand = [self.deck.card_list[0], self.deck.card_list[1]]
        self.card_values_dict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
                                                 'J':10,'K':10,'Q':10}

    # def _eq_ (self):
    #     return
    #
    def __repr__(self):
        return str(self.hand_sum)

    def hand_score(self):
        hand_sum = 0
        hand_in = self.hand
        hand_in_split = []
        values_list = list(self.card_values_dict.values())
        keys_list = list(self.card_values_dict.keys())

        for i, value in enumerate(hand_in):
            for card in value:
             hand_in_split.append(card.split(' '))

        for i in hand_in_split:
            if i in keys_list:
                hand_sum = sum(values_list(i))

        if 'A' in hand_in_split:
            if hand_sum <= 11:
                hand_sum += 10

        return


    def add_card_to_hand (self):
        hand_add = self.hand
        hand_add.append(Deck.draw_card_from_top())
        return

    def user_inputed_hand(self):
        #hand_input = input('Enter up to 4 cards you would like to play ->')
        hand_input  = '10s, Qc,Ad,2h'
        return

def main():
    my_hand = Hand()

    print(repr(Hand))

if __name__ == '__main__':
    main()




