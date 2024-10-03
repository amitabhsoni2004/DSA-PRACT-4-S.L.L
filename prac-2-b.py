# Performing a Binary search in 1D array

def create_array(num):
    # Prompt user to enter elements
    print("Enter Elements now...")
    arr = []  # Initialize an empty list
    for i in range(1, num + 1):
        # Get each element from the user and append to the list
        a = int(input(f"Enter Element no {i}: "))
        arr.append(a)
    
    # Sort the array in ascending order
    arr.sort()
    return arr  # Return the sorted array

def binary_search(arr, num_to_find, start, end):
    # Perform binary search
    while start <= end:
        mid = (start + end) // 2  # Calculate the middle index
        if arr[mid] == num_to_find:
            return mid  # Element found, return index
        elif arr[mid] < num_to_find:
            start = mid + 1  # Search in the right half
        else:
            end = mid - 1  # Search in the left half
    return -1  # Element not found, return -1

def main():
    # Get the number of elements from the user
    num = int(input("Enter the number of elements: "))
    arr = create_array(num)  # Create and sort the array
    
    # Get the number to find from the user
    num_to_find = int(input("Enter the number to find: "))
    # Perform binary search
    index = binary_search(arr, num_to_find, 0, len(arr) - 1)

    if index != -1:
        # Element found, print the index
        print(f"Element {num_to_find} found at index {index}")
    else:
        # Element not found
        print(f"Element {num_to_find} not found in the array")

# Run the program
main()
