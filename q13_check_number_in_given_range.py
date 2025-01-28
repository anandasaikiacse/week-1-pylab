# 13) Python program to check if a number is in a given range.

# input a number
number = int(input("Enter a number: "))

# input the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# check if the number is in the range
if start <= number <= end:
    print(f"{number} is in the range [{start}, {end}].")
else:
    print(f"{number} is not in the range [{start}, {end}].")