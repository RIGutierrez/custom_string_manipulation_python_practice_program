# get user input
user_input = input("Enter your text: ")

# initialize
output = ""

# check first character and convert the characters
if user_input:
    first_character = user_input[0]
    if "a" <= first_character <= "z":
        first_character = chr(ord(first_character) - 32)
    output += first_character

    for character in  user_input[1: ]:
        if "A" <= character <= "Z":
            character = chr(ord(character) + 32)
        output += character

# print
print(output)