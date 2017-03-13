

Class Card(object):

suit_names = ['clubs','diamonds','hearts','spades']
card_ranks = ['ace', '2','3','4','5','6','7','8','9','10','jack','quesn','king']

    def _init_ (self, suit_names, card_ranks):
        self.suit = suit_names
        self.rank = card_ranks

    # def _eq_ (self):
    #     return

    def _repr_(self):
        return ('%r! of %r!')(self.rank, self.suit)


        # def main():
        #     run_again_flag = True
        # while (run_again_flag == True):
        #     in_str = list(input("Please input a credit card number: "))
        #     in_str_numbers = [int(x) for x in in_str]
        #     result = check_card_num(in_str_numbers)
        #     if result == True:
        #         print ("Passed checksum.")
        #     else:
        #         print("Failed Checksum")
        #     run_again = input('Run Again.')
        #     if run_again.lower() not in CONTINUE_PROCESSING_CHARACTERS:
        #         run_again_flag = False
        # if __name__ == '__main__':
        #     main()