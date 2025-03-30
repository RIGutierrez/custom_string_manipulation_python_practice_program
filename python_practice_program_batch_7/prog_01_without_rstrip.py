# get user input
user_input = input("Enter your text: ")

# initialize value from last character
start = len(user_input) - 1

# loop until non-space character is found (right side)
while start >= 0 and user_input[start] == " ":
    start -= 1

# extract substring
user_output = user_input[:start + 1]

# print
print(user_output)