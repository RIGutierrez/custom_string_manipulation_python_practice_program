# get user input
user_input = input("Enter your text: ")
remove_prefix = input("Enter the prefix to remove: ")

# check if input start with the prefix
if user_input.startswith(remove_prefix):
    user_output = user_input.replace(remove_prefix, "", 1)
else:
    user_output = user_input

# print
print(user_output)