# Factorial using Recursion

# Define a function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Take user input and convert it to an integer
num = int(input("Enter a number : "))

# Print the factorial of the given number
print(f"The factorial of given number is : {factorial(num)}")