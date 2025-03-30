# get user input 
user_input = input("Enter your text: ")

# initialize
lowercase_output = ""

# loop through characters
for character in user_input:
    if "A" <= character <= "Z":
        lowercase_output += chr(ord(character) + 32)
    else:
        lowercase_output += character

# print 
print(lowercase_output)