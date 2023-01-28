#Manuel Aragon
#CSCE 4290 Natural Language Processing
#Assignment 1
import currency
import date
import phone_numbers
import tags

file_name = "input.txt"
valid1 = False
valid2 = False 
valid3 = False
valid4 = False
with open(file_name, "r") as file:
    for line_number , line in enumerate(file, 1):
        print('')
        print("Input Line" + str(line_number) + ":\"" + line + "\"")

        print("(1)Checking for Currency:")
        valid1 = currency.is_valid_currency(line)

        print("(2)Checking for Valid dates:")
        valid2 = date.is_valid_date(line)

        print("(3)Checking for Valid phone numbers:")
        valid3 = phone_numbers.is_valid_phone_number(line)

        print("(4) Checking that the string does not contain html tags)")
        valid4 = tags.contains_tags(line)

        if valid1:
            print("This string contains a valid currency.")
        if valid2:
            print("This string contains a valid date.")
        if valid3:
            print("This string contains a valid telephone number.")
        if valid4:
            print("This string contains html tags")