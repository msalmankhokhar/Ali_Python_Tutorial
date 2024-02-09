import random
char ="abcdefghijklmnopqrst@$!#$%^&*()_+=-"
length = 8
password = ""
for a in range(length):
    password+=random.choice(char)
print(password)