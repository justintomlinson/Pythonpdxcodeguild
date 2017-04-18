





# #indexes for string
# i = 'snake_case'
# print(i.find("_"))
# x= i.find("_") # = 5

#working = 'BlueGreen'
#string_length = len(working)
#index = [i for i, e in enumerate(working) if e.isupper()]

# new = []
# inc = 0
# for index, char in enumerate(working[1:], 1):
#     if char.isupper():
#         new.append(working[inc:index])
#         inc = index
# if inc <len(working):
#     new.append(working[inc:])
#     print(new)



#for j in range(0,string_length):
#    if working[j].isupper

#with open('inputfile.txt', newline ='') as inputfile:
#    for row in csv.reader(inputfile):
#        results.append(row)

# with open('inputfile.txt',newline ='') as inputfile:
#     results = list(csv.reader(inputfile))
# print(results)




#split = working.split()
#print(split)


# def find_sum_pairs(int_list, sum):
#     """
#     >>> find_sum_pairs([-1, 0, 1, 2], 3)
#         [[1, 2]]
#     >>> find_sum_pairs([-1, 0, 1, 2], 1)
#         [[-1, 2], [0, 1]]
#     >>> find_sum_pairs([2, -1, 2], 1)
#         [[2, -1], [-1, 2]]
#     >>> find_sum_pairs([-1, 1, 2, 2], 3)
#         [[1, 2], [1, 2]]
#
#     :param int_list:
#     :param sum:
#     :return:
#     """
#     return
list = [-1, 0, 1, 2]
num = 3
nl =[]


lst = [-1,0,1,2]

for index, val in enumerate(lst):
    for i in lst[index+1:len(lst)]:
     if (val + lst[i] == num):
         nl.append([val,(lst[i])])
print(nl)







