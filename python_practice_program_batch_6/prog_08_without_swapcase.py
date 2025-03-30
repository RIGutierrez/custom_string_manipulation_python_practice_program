# get user input
user_input = input("Enter your text: ")

# initialize
output = ""

# loop through characters
for character in user_input:
    if "A" <= character <= "Z":
        output += chr(ord(character) + 32)
    elif "a" <= character <= "z":
        output += chr(ord(character) - 32)
    else:
        output += character

# print
print(output)