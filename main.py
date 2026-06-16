import random

print("====Password Generator====")
print()

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

number = input("Input the number of passwords to generate: ")
number = int(number)
length = input("Input password length: ")
length = int(length)
print()

for pwd in range(number):
  passwords = ""
  for i in range(length):
    passwords += random.choice(chars)
  print(passwords)
