# get user input and prefix to be checked
user_input = input("Enter the text: ")
prefix = input("Enter the prefix to check: ")

# check prefix
if not prefix:
    output = True 
else:
    # remove first part of input and compare with prefix
    output = user_input[:len(prefix)] == prefix

# print
print(output)