"""This program handles case conversions on in user prompted words"""


def case_format_find(user_input):
    """This function defines the case of the user's input
    >>> case_format_find('snake_case')

    >>> case_format_find('CamelCase')

    >>> case_format_find('kebab-case')

    >>> case_format_find('CONSTANT_CASE')

    :return:
    """
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
    >>> case_change_intermediate('snake_case')

    >>> case_change_intermediate('CamelCase')

    >>> case_change_intermediate('kebab-case')

    >>> case_change_intermediate('CONSTANT_CASE')


    :return:
    """
    working = user_input
    new_list = []
    inc = 0

    if case_type == 'snake':
        split = working.split("_")
    elif case_type == 'kebab':
        split = working.split("-")
    elif case_type == 'constant':
        split = (working.lower()).split("-")
    else:
        for index, char in enumerate(working[1:], 1):
            if char.isupper():
                new_list.append(working[inc:index])
                inc = index
        if inc < len(working):
            new_list.append(working[inc:])
        split = [x.lower() for x in new_list]

    return (split)

def case_change_final(split,new_format):
    """This function converts an agnostic version of the user input word from case_change_intermediate to the user
    requested case format.
    >>> case_change_final('snake_case')

    >>> case_change_final('CamelCase')

    >>> case_change_final('kebab-case')

    >>> case_change_final('CONSTANT_CASE')


    :return:
    """
    case_change = ''

    if new_format == 'camel':
        case_change = ''.join([y.capitalize() for y in split])
    elif new_format == 'snake':
        case_change = '_'.join(split)
    elif new_format =='kebab':
        case_change = '-'.join(split)
    else:
        case_change = '-'.join([y.upper() for y in split])

    return(case_change)

# def output_case(change_case):
#     """ This function determines the out going case format of the convert word.
#     >>> output_case('snake_case')
#
#     >>> output_case('CamelCase')
#
#     >>> output_case('kebab-case')
#
#     >>> output_case('CONSTANT_CASE')
#
#     :return:
#     """
#      results = print('user input = ' + str(user_input), case)
#     return ()


def main ():
    """This function establishes user inputs and calls the other functions to determine the case format and change ot
     as the user desires.

    :return:
    """
    user_input = str(input('Please provide a word in snake_case, CamelCase, kebab-case, or CONSTANT_CASE ->'))
    new_format = str(input('Please select the format you would like to convert to: snake, camel, kebab, constant - >'))
    orig_format = case_format_find(user_input)
    interm_chagne = case_change_intermediate(user_input, orig_format)
    output_word = case_change_final(interm_chagne, new_format)

    print('Entered format = ' + str(orig_format))
    print('Changed to ->' + str(output_word))


if __name__ == '__main__':
    main()

