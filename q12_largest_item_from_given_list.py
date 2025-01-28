# 12) Python program to find the largest item from a given list.

# input a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# Find the largest number using max() function
largest = max(numbers)

# Print the result
print("The largest number in the list is:", largest)




# OR (using loop):




# input a list of numbers
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))

# initialize the largest variable to the first element of the list
largest = numbers[0]

# Loop through the list to find the largest number
for number in numbers:
    if number > largest:
        largest = number
        
# Print the result
print("The largest number in the list is:", largest)