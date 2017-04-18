c_numlist = [4,5 ,5 ,6 ,7 ,3 ,7 ,5 ,8 ,6 ,8 ,9 ,9 ,8, 5, 5]
def last_digit_slice():
    """ Removes the last digit from an entered list and updates the list

    :return:
    >>>>last_digit_slice(c_numlist_1], check_digit)
    [4,5 ,5 ,6 ,7 ,3 ,7 ,5 ,8 ,6 ,8 ,9 ,9 ,8, 5], [5]
    """
    check_digit = c_numlist.pop()
    c_numlist_1 = c_numlist[0:(len(c_numlist))]
    return(check_digit)

def reverse_the_digits(c_numlist_1):
    """ This function reverse the digits of a entered list

    :return:
    """
    c_numlist_2 = c_numlist_1.reverse()
    return

def multiply_even_digits (c_numlist_2):
    """This function multiples the even_indexed reversed digits by two
    >>>>multiply_even_digits(    )
    :return:
    """

for i in c_numlist_2[::2]:
    c_numlist_3[i] = c_numlist_2[1]*2

return(c_numlist_3)
