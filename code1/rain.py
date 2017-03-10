""" Rain """

#def import_data_file('filename')
with open('raintest.txt')as rain_data_file:
    rain_list= rain_data_file.readlines()
    just_data =[]


    start = 0
for i,line in enumerate(rain_list):
    if line.startswith('-----'):
        start = i+1
        break

for data in rain_list[11:len(rain_list)]: # you cheated fix this later
        just_data.append(data.split())

#data_splitdate =[]
#for i in range(0,len(just_data)):
#    just_data[i][0].split('-')

rain_dict = {d[0]:int(d[1])for d in just_data}
print(rain_dict)

#def find_most_rain by_date(rain_dict)
max_rain = max(rain_dict.items(), key=lambda k: k[1])
print(max_rain)
#from sample -('06-FEB-2015', '96')


#def find_year_with_most_rain(rain_dict):
# import datetime
# date_format = '%d-%m-%Y'
# x= rain_dict
# for i in x:
#     datetime= datetime.datetime.strptime(x.keys(),date_format)


# list_rain_dict = list(rain_dict.items())
#
# for item in list_rain_dict:
#     for key, value in item.iteritems():
#         item[key] = int(value)
# print(list_rain_dict)
#
# # r_dict_mod = [dict([a, int(x)] for a, x in rain_dict.iteritems())for ]
# # for x in rain_dict.values():
# #     print(int(rain_dict.values()))
#
#def group_by(iterable, key):
#    """Place each item in an iterable into a bucket based on calling the key
#    function on the item."""
group_to_items = {}
for item in rain_dict:
   group = item[7:11]
   if group not in group_to_items:
      group_to_items[group] = []
      group_to_items[group].append(item)
#return group_to_items
print(group_to_items)

#for x, y in rain_dict.items():

#print(year)
#         yr16 = sum(rain_dict.values())
#     elif x[7:11] == '2015':
#         yr15 = sum(rain_dict.values())
#     elif x[7:11] == '2014':
#         yr14 = sum(rain_dict.values())
#     elif x[7:11] == '2013':
#         yr13 = sum(rain_dict.values())
#     elif x[7:11] == '2012':
#         yr12 = sum(rain_dict.values())
#
# print (str(yr16))
# print (str(yr15))