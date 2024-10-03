# Fibonacci series 

def fibonacci(n):
    # Initialize the first two terms of the Fibonacci series
    n1 = 0
    n2 = 1
    # Print the first two terms
    print(f"{n1} {n2} ", end="")

    # Loop to generate the next terms in the series
    for i in range(2, n):
        # Calculate the next term
        n3 = n1 + n2
        # Print the next term
        print(f"{n3} ", end="")
        # Update the previous two terms
        n1 = n2
        n2 = n3

# Get the number of terms from the user
num = int(input("Enter a number of terms: "))
# Call the function to print the Fibonacci series
fibonacci(num)