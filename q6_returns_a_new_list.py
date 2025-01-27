# 6) Python program to get a new list with unique elements from a given list

# input a list
input_list = input("Enter elements of the list separated by space: ").split()

# Get unique elements using list comprehension
unique_list = []
[unique_list.append(item) for item in input_list if item not in unique_list]

# print the result
print("Unique elements:", unique_list)