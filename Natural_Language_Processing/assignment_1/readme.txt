Manuel Aragon
CSCE 4290 NATURAL LANGUAGE PROCESSING
ASSIGNMENT 1

Written using Python3 3.10.6

HOW TO RUN:
In order to run change to directory that contains driver.py and run the command:
'python3 driver.py'

INPUT FILE:
The input of the code is the input.txt file. It has examples of valid currencies,
phone numbers, dates, and html tags. 

HOW IT WORKS:
The driver file will read each line and input it into four functions to check for
valid currencies, phone numbers, dates, and html tags. The output of each function
will be printed to the screen.


EXAMPLE OF OUTPUT:
Input Line2:"The total cost for the project came out to $954.49.
"
(1)Checking for Currency:
<re.Match object; span=(43, 50), match='$954.49'>
(2)Checking for Valid dates:
None
None
None
None
(3)Checking for Valid phone numbers:
None
(4) Checking that the string does not contain html tags)
None
This string contains a valid currency.