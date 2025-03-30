# get user input
user_input = input("Enter your text: ")

# initialize
is_lower = True

# loop through characters
for character in user_input:
    if "A" <= character <= "Z":
        is_lower = False
        break  

# print
print(is_lower)