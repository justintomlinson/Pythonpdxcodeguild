card_one = input("What is your first card? ---> ")
card_two = input ("What is your second card? ---> ")
card_three = input("What is your third card? ---> ")

card_total = 0

number_cards = ["2", "3", "4", "5", "6", "7", "8" ,"9"]
face_cards = ["10","J", "Q", "K"]
ace_card =1

if card_one in face_cards:
   card_one = 10
   print (card_one)
elif card_one in number_cards:
     print (card_one)
else:
    card_one = 1
    print (card_one)

if card_two in face_cards:
    card_two = 10
    print (card_two)
elif card_two in number_cards:
    print (card_two)
else:
    card_one = 1
    print (card_two)

if card_three in face_cards:
    card_three = 10
    print (card_three)
elif card_three in number_cards:
    print (card_three)
else:
    card_three = 1
    print (card_three)


card_total = int(card_one) + int(card_two) + int(card_three)
print(card_total)

