"""Reviews """

import json

from collections import namedtuple

namedtuple('UserData', ['user_name', 'user_city'])
namedtuple('BusinessData', ['business_name', 'business_city'])
namedtuple("ReviewData", ['user_name', 'business_name', 'rating', 'review_text'])

business_file_dict = {}
with open('businesses.txt')as business_file:
    for line in business_file.readlines():
       business_file_dict.update(json.loads(line))
print(business_file_dict)
BusinessData = namedtuple()
business = BusinessData(('voodoo donuts'),('dicks burgers'), ('portland','seattle'))
print(business)








