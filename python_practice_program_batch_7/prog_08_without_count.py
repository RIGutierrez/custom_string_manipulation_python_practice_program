# get user input and text to be counted in text
user_input = input("Enter your text: ")
text_to_count = input("Enter the text to count: ")

# initialize
count = 0
index = 0

# loop through characters
while index <= len(user_input) - len(text_to_count):
    if user_input[index : index + len(text_to_count)] == text_to_count:
        count += 1
    index += 1

# print
print(count)