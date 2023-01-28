#Manuel Aragon
#CSCE 4290 Natural Language Processing
#Assignment 1
import re

def is_valid_currency(string):
    regex = re.compile(r'([+-]?[$]([\d]{1,3},?)*([.]\d{2})?|[A-Z]{3}\d*)(K|M|B|T)?')
    match = regex.search(string)
    print(match)
    if (match == None):
        return False
    else:
        return True