""" This progroam reads a file and reformats """

#def import_file (inputfile):
#    """

#   :return:
#    """
import csv

results= []
#with open('inputfile.txt', newline ='') as inputfile:
#    for row in csv.reader(inputfile):
#        results.append(row)

# with open('inputfile.txt',newline ='') as inputfile:
#     results = list(csv.reader(inputfile))
# print(results)
# # #    return

with open('inputfile.txt') as input_data:
    file_lines = input_data.readlines()

new = []
new2 =[]
print(file_lines)
for index, value in enumerate(file_lines):
       for i, elem in enumerate(value):
           new.append(((value.strip('\n')).split(' ')))
       print(new)
new_mod = []



#print(new_mod1)


max_length = [max(len(str(x))for x in column)for column in zip(*new)]
print(max_length)

# for index, elem in enumerate(new):
#     if index != len(new):
#         new_mod.append((elem).split(','))

print(new_mod)
# def make_partition_line(max_length):
for i, col in enumerate(max_length):
    make_line = str('|'+('-'*max_length[i]))
#    return(make_line)

#insert_line = (str('|'+'-'*col_len +'|', end = ''))
print('|')
for index, value in enumerate(new):
    if index < 2:
        print((make_line), end = '')
        for i, item in enumerate(value):
            print(make_line, end = '',)

print('|')








# for index, char in enumerate(working[1:], 1):
#     if char.isupper():
#         new_list.append(working[inc:index])
#         inc = index
# if inc < len(working):
#     new_list.append(working[inc:])
# split = [x.lower() for x in new_list]
