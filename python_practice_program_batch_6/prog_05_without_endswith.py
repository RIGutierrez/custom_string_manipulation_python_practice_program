# get user input and suffix to be checked
user_input = input("Enter the text: ")
suffix = input("Enter the suffix to check: ")

# check suffix
if not suffix:
    output = True
else:
    # remove last part of input and compare with suffix
    output = user_input[-len(suffix):] == suffix

# print
print(output)