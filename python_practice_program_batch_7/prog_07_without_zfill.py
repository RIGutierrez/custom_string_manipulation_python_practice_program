# get user input
user_input = input("Enter the text: ")
width_input = int(input("Enter the total width: "))

# add zero if the text is shorter than width
if len(user_input) < width_input:
    output = "0" * (width_input - len(user_input)) + user_input 
else: 
    output = user_input

# print
print(f"'{output}'")