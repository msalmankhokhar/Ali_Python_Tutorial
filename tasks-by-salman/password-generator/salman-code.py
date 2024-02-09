from random import choice
import string
from os import system

digits = string.digits
choti_abc = string.ascii_lowercase
bari_abc = string.ascii_uppercase
symbols = [ '@', '$', '#', '%', '&', '*', '!' ]

options = [ choti_abc ]

include_capital_letters = True
include_digits = True
include_symbols = True

length_of_password = input("Enter length of password: ")
while True:
    try:
        length_of_password = int(length_of_password)
        break
    except Exception as error:
        print("Wrong Input. Try again")
        length_of_password = input("Enter length of password: ")

input_for_capitalLetters = input("Include capital letters? (Default: yes) (y/n)")
while True:
    if include_capital_letters == 'y' or input_for_capitalLetters == 'n' or input_for_capitalLetters == '':
        if input_for_capitalLetters == 'n':
            include_capital_letters == False
        else:
            options.append(bari_abc)
        break
    else:
        print("Wrong Input. Try again")
        input_for_capitalLetters = input("Include capital letters? (Default: yes) (y/n)")
        
input_for_digits = input("Include digits/numbers? (Default: yes) (y/n)")
while True:
    if input_for_digits == 'y' or input_for_digits == 'n' or input_for_digits == '':
        if input_for_digits == 'n':
            include_digits = False
        else:
            options.append(digits)
        break
    else:
        print("Wrong Input. Try again")
        input_for_digits = input("Include digits/numbers? (Default: yes) (y/n)")

input_for_symbols = input("Include symbols? (Default: yes) (y/n)")
while True:
    if input_for_symbols == 'y' or input_for_symbols == 'n' or input_for_symbols == '':
        if input_for_symbols == 'n':
            include_symbols = False
        else:
            options.append(symbols)
        break
    else:
        print("Wrong Input. Try again")
        input_for_symbols = input("Include symbols? (Default: yes) (y/n)")

password = ''

for n in range(length_of_password):
    option = choice(options)
    password += choice(option)

print(f"Your password is \n{password}\nof length {len(password)}")