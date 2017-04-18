""" This progroam reads a file and reformats """

#def import_file (inputfile2):
#    """ Import text files and reads the file into a list

#   :return: file_lines
#    """
with open('inputfile2.txt') as input_data:
    file_lines = input_data.readlines()
#   retun(file_lines)

def format_to_list(file_lines):
    """

    :param file_lines:
    :return:
    """

new_list = []
for value in file_lines:
    new_list.append((value.strip('\n')).split(','))

work_list = []
for sublst in new_list:
    for item in sublst:
        work_list.append(','.join(sublst).split(' '))
#   return(work_list)

# #def find_column_length(work_list):
#     """Finds the length of each string a list and then finds the max length out of all strings in that column
#
#     :param work_list:
#     :return:
#     """
max_length = [max(len(str(x))for x in column)for column in zip(*work_list)]
#   return(max_length

# #def create_empty_line(max_length):
#     """
#
#     :param max_length:
#     :return:
#     """
for i, col in enumerate(max_length):
    make_line = str('|'+('-'*max_length[i]))
#    return(make_line)


print(make_line
print(str(work_list[0]), end = '')
print(make_line+'|', end = '')

for i in work_list[1:len(work_list)]:
    print(str(work_list[i]))


# for index, value in enumerate(work_list):
#      print(value)
#      if index < 2:
#           print( make_line +'|', end = '')
#           for i, item in enumerate(value):
#              print(make_line, end = '',)









