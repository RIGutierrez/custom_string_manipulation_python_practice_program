# get user input and character/text to find
user_input = input("Enter your text: ")
target_character = input("Enter the character to find: ")

# loop through characters and check if the character/text to be find exists
for i in range(len(user_input) - len(target_character) + 1):
   
    # check if character/text matches
    if user_input[i:i+len(target_character)] == target_character:
        
        # print
        print(i)
        break
else:
    print("Target character/text not found")