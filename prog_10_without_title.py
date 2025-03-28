# get user input
user_input = input("Enter your text: ")

# initialize
output = ""
capitalize_next = True

# loop through characters
for character in user_input:
    if "a" <= character <= "z":
        if capitalize_next:
            output += chr(ord(character) - 32)
        else:
            output += character
        capitalize_next = False
    elif "A" <= character <= "Z":
        if not capitalize_next:
            output += chr(ord(character) + 32)
        else:
            output += character
        capitalize_next = False
    else:
        output += character
        capitalize_next = True
            
# print 
print(output)