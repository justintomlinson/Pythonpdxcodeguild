""" This progroam reads a file and reformats """

#def import_file (inputfile):
#    """

#   :return:
#    """
import csv



with open('inputfile.txt') as input_data:
    file_lines = input_data.readlines()


new_list = []
for index, value in enumerate(file_lines):
    new_list.append((value.strip('\n')).split(','))
#
work_list = []
for sublst in new_list:
    for item in sublst:
        work_list.append(','.join(sublst).split(' '))

max_length = [max(len(str(x))for x in column)for column in zip(*work_list)]


# # for index, elem in enumerate(new):
# #     if index != len(new):
# #         new_mod.append((elem).split(','))
#
# # def make_partition_line(max_length):
for i, col in enumerate(max_length):
    make_line = str('|'+('-'*max_length[i]))
#    return(make_line)

#insert_line = (str('|'+'-'*max_length +'|', end = ''))
print('|'+ make_line)
for index, value in enumerate(work_list):
    print(value)
     if index < 2:
         print(work_list + make_line, end = '')
         for i, item in enumerate(value):
             print(make_line, end = '',)

print('|')








