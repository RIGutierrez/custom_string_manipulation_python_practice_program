# get user input
user_input = input("Enter your text: ")
remove_suffix = input("Enter the suffix to remove: ")

# check if input ends with the suffix
if user_input.endswith(remove_suffix):
    output = user_input[:-len(remove_suffix)] 
else:
    output = user_input

# print
print(output)