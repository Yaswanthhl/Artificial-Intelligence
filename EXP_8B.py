import string

my_str = input("Enter String: ")
words = my_str.split(".")
words.sort()
for word in words:
  print(word)