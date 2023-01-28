#Manuel Aragon
#CSCE 4290 Natural Language Processing
#Assignment 1
import re

def contains_tags(string):
    date_regex = re.compile(r'<[/]?[a-zA-Z][^>]*>')
    match = date_regex.search(string)
    print(match)

    if(match):
        return True
    else:
        return False