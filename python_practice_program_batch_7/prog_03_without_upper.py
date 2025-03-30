# get user input
user_input = input("Enter your text: ")

# initialize
uppercase_output = ""

# loop through characters
for character in user_input:
    if "a" <= character <= "z":
        uppercase_output += chr(ord(character) - 32)
    else:
        uppercase_output += character

# print
print(uppercase_output)