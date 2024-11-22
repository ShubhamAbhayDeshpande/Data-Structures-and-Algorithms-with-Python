"""
This file is a basic introduction to recursion and how we can use recursion to solve 
multiple kinds of problems. The main goal of this file is to see tha "call stack".

The example problem used here is a factorial.
"""
def myFactorial(number):
    if number == 0:
        return 1
    return number * myFactorial(number-1)


if __name__ == "__main__":
    num = int(input("Enter any integer: "))
    print(f"Factorial of {num}: ", myFactorial(num))
    
