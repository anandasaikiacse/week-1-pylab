# 14) Python program to count the number of uppercase and lowercase letters in a string.

# input a string
string = input("Enter a string: ")

# initialize the count variables
uppercase_count = 0
lowercase_count = 0

# loop through the string to count uppercase and lowercase letters
for char in string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
        
# print the result
print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")



# OR (using isupper() and islower() functions directly):



# input a string
string = input("Enter a string: ")

# Count the number of uppercase and lowercase letters using list comprehension
uppercase_count = sum(1 for char in string if char.isupper())
lowercase_count = sum(1 for char in string if char.islower())

# print the result
print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")