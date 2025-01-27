# 10) Python program to check if a number is prime or not

# input a number
number = int(input("Enter a number: "))

# check if the number is prime
if number > 1:
    for i in range(2, int(number ** 0.5) + 1):
        if (number % i) == 0:
            print(number, "is not a prime number.")
            break
    else:
        print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")