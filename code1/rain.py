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

data_splitdate =[]
for i in range(0,len(just_data)):
    just_data[i][0].split('-')



rain_dict = {d[0]:d[1]for d in just_data}


#def find_most_rain by_date(rain_dict)
max_rain = max(rain_dict.items(), key=lambda k: k[1])
print(max_rain)
#from sample -('06-FEB-2015', '96')


#def find_year_with_most_rain(rain_dict):
import datetime
date_format = '%d-%m-%Y'
x= rain_dict
for i in x:
    datetime= datetime.datetime.strptime(x.keys(),date_format)
#
