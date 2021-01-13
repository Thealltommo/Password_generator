#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

ch_letters = ""
ch_symbols = ""
ch_numbers = ""

for c in range(nr_letters):
  ch_letters += random.choice(letters) #  select random choice of letters from user input
  
for s in range(nr_symbols):
  ch_symbols += random.choice(symbols)

for n in range(nr_numbers):
  ch_numbers += random.choice(numbers)

password = (ch_letters + ch_symbols + ch_numbers) #  password

print(f"Your password is  \n{password}")

password = list(password) #  make password a list so it can be shuffled as str not supported by .shuffle

random.shuffle(password) #  shuffle password around for higher difficulty
password = "".join(password)
print(password)
