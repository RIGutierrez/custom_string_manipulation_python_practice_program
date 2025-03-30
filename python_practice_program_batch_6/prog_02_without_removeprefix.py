# get user input
user_input = input("Enter your text: ")
remove_prefix = input("Enter the prefix to remove: ")

# check if input starts with the prefix
if user_input.startswith(remove_prefix):
    output = user_input.replace(remove_prefix, "", 1)
else:
    output = user_input

# print
print(output)