import random
chars = "abcdefghijklmnopqrstuvwxyz"+"ABCDEFGHIJKLMNOPQRSTUVWXY"+"012345679"+"!@#$%^&*()_+=*/[]}{?.,;:"
length = int(input("Password length: "))
number = int(input("Enter number of passwords you want: "))
for i in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)
    print("Generated password: ",password)
        