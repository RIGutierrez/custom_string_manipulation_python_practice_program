# get user input
user_input = input("Enter the text: ")
width_input = int(input("Enter the total width: "))

# check if width is not smaller than length of text
if width_input > len(user_input):    
    # calculate spaces to be add 
    total_spaces = width_input - len(user_input)
    left_spaces =  total_spaces // 2
    right_spaces = total_spaces - left_spaces
    
    # centralize the user input
    output = " " * left_spaces + user_input + " " * right_spaces
else:
    output = user_input

# print
print(f"'{output}'")