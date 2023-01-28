#Manuel Aragon
#CSCE 4290 Natural Language Processing
#Assignment 1
import re

def is_valid_date(string):
    date_regex_1 = re.compile(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s\d{2},\s\d{4}$')
    date_regex_2 = re.compile(r'\d{1,2}[/-]\d{1,2}[/-]\d{2}')
    date_regex_3 = re.compile(r'\d{1,2}-[A-Za-z]{3}, \d{4}')
    date_regex_4 = re.compile(r'\d{4}[/-]\d{1,2}[/-]\d{2}')
    match1 = date_regex_1.search(string)
    match2 = date_regex_2.search(string)
    match3 = date_regex_3.search(string)
    match4 = date_regex_4.search(string)

    print(match1)
    print(match2)
    print(match3)
    print(match4)
    if(match1 or match2 or match3 or match4):
        return True