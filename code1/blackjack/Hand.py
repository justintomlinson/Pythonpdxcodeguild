"""This module creates and scores a hand of blackjack. It will alert the user if they are over 21 """
import Deck
import Card


class Hand:
    def __init__ (self, deck_in):
        """ Establish hand with 2 cards

        :return:
        """
        self.deck = deck_in
        self.hand = [self.deck.card_list[0], self.deck.card_list[1]]
        self.card_values_dict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10,
                                                 'J':10,'Q':10,'K':10}

    # def _eq_ (self):
    #     return
    #
    def __repr__(self):
        """

        :return:
       >>>  hand_sum = 21
       'BUST!'
        """
        if self.hand_sum > 21:
            return ('BUST!')


    def hand_score(self):
        """ This function calculates the score of a users hand.

        :return:
        >>> Hand.hand_score()
         13
        """
        hand_sum = 0
        hand_in = self.hand
        hand_in_split = []
        values_list = list(self.card_values_dict.values())
        keys_list = list(self.card_values_dict.keys())

        for i, value in enumerate(hand_in):
            for card in value:
             hand_in_split.append(card.split(' '))

        new_hand_list = [item for sublist in hand_in_split for item in sublist]

        for i in new_hand_list:
            if i in keys_list:
                hand_sum += (self.card_values_dict[i])

        if 'A' in new_hand_list:
            if hand_sum <= 11:
                hand_sum += 10
            else: hand_sum

        return hand_sum


    def add_card_to_hand (self):
        """

        :return:
        >>>

        """
        hand_add = self.hand
        hand_add.append(Deck.Deck.draw_card_from_top(self.deck))

        return

    def user_inputed_hand(self):
        #hand_input = input('Enter up to 4 cards you would like to play ->')
        hand_input  = '10s, Qc,Ad,2h'
        return

def main():
    deck_in = Deck.Deck()
    myhand = Hand(deck_in)
    score = myhand.hand_score()
    print(score)
    # add_card = Hand.add_card_to_hand(myhand)
    # if score < 15:
    #     add_card
    # else: print(repr(myhand))

if __name__ == '__main__':
    main()




