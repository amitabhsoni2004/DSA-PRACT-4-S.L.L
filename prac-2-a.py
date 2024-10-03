# Performing Linear search on 1D array

# Function to create an array of given size
def array_create(num):
    print("Enter elements in array now...")
    arr = []  # Initialize an empty list
    for i in range(1, num + 1):  # Loop to get array elements from user
        a = int(input(f"Enter Element no {i} : "))  # Input element
        arr.append(a)  # Append element to the list
    return arr  # Return the created list

# Function to perform linear search on the array
def linear_search(arr, num_to_find):
    for i in range(len(arr)):  # Loop through each element in the array
        if arr[i] == num_to_find:  # Check if current element is the one we are looking for
            print(f"Element found at index {i}")  # Print the index if element is found
            return  # Exit the function
    print("Element is not in Array")  # Print message if element is not found

# Main function to drive the program
def main():
    num = int(input("Enter number of terms to determine size of array: "))  # Input size of array
    arr = array_create(num)  # Create array of given size
    num_to_find = int(input("Enter a number to find: "))  # Input the number to search for
    linear_search(arr, num_to_find)  # Perform linear search

main()  # Call the main function to execute the program