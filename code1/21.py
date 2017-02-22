
card_one = input("What is your first card? ---> ")
card_two = input ("What is your second card? ---> ")
card_three = input("What is your third card? ---> ")

card_total = 0

number_cards = ["2", "3", "4", "5", "6", "7", "8" ,"9"]# list of available non-face cards
face_cards = ["10","J", "Q", "K"]# list of face cards with uniform value of 10
ace_card =1
#Determines the value of the first card from inputed value
if card_one in face_cards:
   card_one = 10
elif card_one in number_cards:
    card_one == (card_one in number_cards)
#elif card_one == "A":
#    if int(card_two) + int(card_three) <= 11:
#        card_one == 10
else:
    card_one = ace_card
#Determines the value of the second card from inputed value
if card_two in face_cards:
    card_two = 10
elif card_two in number_cards:
    card_two == (card_two in number_cards)
else:
    card_two = ace_card
#Determines the value of the third card from inputed value
if card_three in face_cards:
    card_three = 10
elif card_three in number_cards:
    card_three == (card_three in number_cards)
else:
    card_three = ace_card
# Calculate the the total value of card inputs
card_total = int(card_one) + int(card_two) + int(card_three)
print(card_total)
#Output response based on sum of inputed values
if card_total < 17:
    print("Hit")
elif 21 > card_total >= 17:
    print ("Stay")
elif card_total == 21:
    print("Blackjack!")
else:
    print("Already busted")


