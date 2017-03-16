""" This is to calculate Oregon income tax based on income level"""

taxrate_one = .05
taxrate_two = .07
taxrate_three = .09
taxrate_four = .099

taxbracket_one= 3350
taxbracket_two = 5050
taxbracket_three = 116600

taxable_income = 0
taxes = 0

income_float = float(input("Please enter your gross income -->"))

if income_float >= taxbracket_one:
    taxes = taxbracket_one*taxrate_one
    income_float = income_float - taxbracket_one
else:
    taxes = income_float*taxrate_one
print (taxes)
print (income_float)

if income_float >= taxbracket_two:
     taxes = taxes + (taxbracket_two * taxrate_two)
     income_float = income_float - taxbracket_two
else:
    taxes = taxes + income_float*taxrate_two
print (taxes)
print (income_float)

if income_float >= taxbracket_three:
    taxes = taxes + (taxbracket_three*taxrate_three)
    income_float = income_float - taxbracket_three
else:
    taxes = taxes + (income_float*taxrate_three)
    income_float = income_float - taxbracket_three
print (taxes)
print (income_float)

if income_float > 0:
     taxes = taxes + income_float*taxrate_four
 #    print("You owe"+ "$" + str(taxes)+ " in taxes")
print (taxes)
print (income_float)


