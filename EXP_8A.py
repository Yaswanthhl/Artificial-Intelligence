import string

test_str = input("Enter String: \n")
modify_str = test_str.translate(str.maketrans("", "", string.punctuation))
print(modify_str)