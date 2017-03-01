"""This program handles case conversions on in user prompted words"""

def define_case(user_input):
    """This function defines the case of the user's input
    >>>define_case('snake_case')

    >>>define_case('CamelCase')

    >>>define_case('kebab-case')

    >>>define_case('CONSTANT_CASE')

    :return:
    """

    user_input = str(input('Please provide a word in snake_case, CamelCase, kebab-case, or CONSTANT_CASE ->'))

    case_type = ''

    if user_input.islower():
        if "_" in user_input:
            case_type = 'snake'
        else: case_type ='kebab'
    elif user_input.isupper():
        case_type = 'constant'
    else:
        case_type = 'camel'

    return(case_type)

def case_change_intermediate(user_input, case_type):
    """This function changes the inputed word into a agnostic representation to be worked on later
    >>>case_change_intermediate('snake_case')

    >>>case_change_intermediate('CamelCase')

    >>>case_change_intermediate('kebab-case')

    >>>case_change_intermediate('CONSTANT_CASE')


    :return:
    """
    working = user_input.copy()

    if case_type == 'snake':
        split = working.split("_")
    elif case_type == 'kebab':
        split = working.split("-")
    elif case_type == 'constant':
        split = working.split("-")
    else:
       for index, char in enumerate(working):
           print(index)
           print(char)



    return (split)

def case_change_final(x, y):
    """This function converts an agnostic version of the word from case_change_intermediate to the new desired case
    format.
    >>>case_change_final('snake_case')

    >>>case_change_final('CamelCase')

    >>>case_change_final('kebab-case')

    >>>case_change_final('CONSTANT_CASE')


    :return:
    """
    split =
    return

def output_case():
    """ This function determines the out going case format of the convert word.
    >>>output_case('snake_case')

    >>>output_case('CamelCase')

    >>>output_case('kebab-case')

    >>>output_case('CONSTANT_CASE')

    :return:
    """
    return



# def main ():
#   user_input = str(input('Please provide a word in snake_case, CamelCase, kebab-case, or CONSTANT_CASE ->'))
    new_format = str
# if __name__ == '__main__':
#     main()

