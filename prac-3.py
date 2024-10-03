# Performing bubble sort in 1D array

# Function to create an array of n elements
def create_arr(n):
    print("Enter elements now...")
    arr = []
    for i in range(1, n + 1):
        a = int(input(f"Enter element {i}: "))  # Take input for each element
        arr.append(a)  # Append element to the array
    return arr

# Function to perform bubble sort on an array
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if elements are in the wrong order
    return arr

# Main function to execute the program
def main():
    num = int(input("Enter number of terms: "))  # Input number of elements
    arr = create_arr(num)  # Create array with input elements
    sorted_arr = bubble_sort(arr)  # Sort the array using bubble sort
    print(f"Sorted Array = {sorted_arr}")  # Print the sorted array

main()  # Call the main function to run the program