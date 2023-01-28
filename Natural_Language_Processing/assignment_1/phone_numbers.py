#Manuel Aragon
#CSCE 4290 Natural Language Processing
#Assignment 1
import re

def is_valid_phone_number(string):
    number_regex_1 = re.compile(r'(\d{10})?([+]\d\s)?(([(]?\d{3}[)]?)?(\s|\-)?){3}(\d{4})')

    match1 = number_regex_1.search(string)


    print(match1)

    if(match1 ):
        return True
    else:
        return False