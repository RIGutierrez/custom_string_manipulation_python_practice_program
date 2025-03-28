# get user input
user_input = input("Enter your text: ")

# initialize variable
start = 0

# loop until non-space character is found
while start < len(user_input) and user_input[start] == " ":
    start += 1

# extract substring
user_output = user_input[start:]

# print
print(user_output)