#Password Generator Project

import random
import re
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@', '^', '-', '_', '=', '']

print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

x = True
while x:  
    if (len(password)<14):
        print("Sorry, but your password contains less than 14 characters. Please try again")
        break
    elif not re.search("[a-z]",password):
        print("Sorry, but your password does not contain at least one lowercase letter. Please try again.")
        break
    elif not re.search("[0-9]",password):
        print("Sorry, but your password does not contain at least one number. Please try again.")
        break
    elif not re.search("[A-Z]",password):
        print("Sorry, but your password does not contain at least one uppercase letter. Please try again.")
        break
    elif re.search("\s",password):
        print("Sorry, but your password  contain the space. Please try again.")
        break
    elif not re.search("[$#@%,.;:*^&!?})\\\({>~<|?/`'\"\[\]]",password):
        print("Sorry, but your password does not contain at least one punctuation character. Please try again.")
        break
    else:
        print(f"Your password is: {password}")
        x=False
        break

if x:
    print("Not a Valid Password")

