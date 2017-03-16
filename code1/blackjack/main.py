import Deck
import Hand
import Card

def main():

    deck_in = Deck.Deck()
    deck_in.shuffle_deck()
    myhand = Hand.Hand(deck_in)
    score = myhand.hand_score()
    print(score)
    if score <= 15:
        print('You should hit')
        # user_input = input('Do you wish to hit (y or n)? - >')
        # if user_input == 'y' :
        #     new_hand = myhand.add_card_to_hand()
        #     new_score = new_hand.hand_score()
        #     print(new_score)
        # else:
        #     print(score)
    elif 15 < score < 21:
        print('You should stay')




if __name__ == '__main__':
    main()