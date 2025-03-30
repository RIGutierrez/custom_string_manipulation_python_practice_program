# get user input
user_input = input("Enter your text: ")

# initialize
is_uppercase = True

# loop through characters
for character in user_input:
    if "a" <= character <= "z":
        is_uppercase = False
        break
# print
print(is_uppercase)