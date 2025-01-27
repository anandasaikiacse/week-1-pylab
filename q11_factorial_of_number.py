# 11) Python program to find the factorial of a number.

# input a number
number = int(input("Enter a number: "))

# initialize factorial to 1
factorial = 1

# calculate the factorial
if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of", number, "is:", factorial)
    
    
    
# OR (using math.factorial()):



import math

# input a number
number = int(input("Enter a number: "))

# calculate factorial using math module
if number < 0:
    print("Factorial does not exist for negative numbers.")
else:
    factorial = math.factorial(number)
    print("The factorial of", number, "is:", factorial)