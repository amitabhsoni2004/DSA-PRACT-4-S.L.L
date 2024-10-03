// performing a bubble sort

#include<iostream> // Include the iostream library for input and output operations
using namespace std; // Use the standard namespace to avoid prefixing std:: before standard functions

// Function to create an array by taking input from the user
void create_arr(int arr[50], int size) {
    cout << "Enter elements now...\n"; // Prompt the user to enter elements
    for (int i = 0; i < size; i++) { // Loop through the array to take input
        cin >> arr[i]; // Store each input element in the array
    }
}

// Function to perform bubble sort on the array
void bubble_sort(int arr[50], int size) {
    int temp; // Temporary variable for swapping
    for (int i = 0; i < size - 1; i++) { // Outer loop for passes
        for (int j = 0; j < size - i - 1; j++) { // Inner loop for comparing adjacent elements
            if (arr[j] > arr[j + 1]) { // If the current element is greater than the next element
                temp = arr[j + 1]; // Swap the elements
                arr[j + 1] = arr[j];
                arr[j] = temp;
            }
        }
    }

    cout << "\nSorted array : \n"; // Print the sorted array
    for (int i = 0; i < size; i++) { // Loop through the sorted array
        cout << arr[i] << " "; // Print each element
    }
}

int main() {
    int arr[50], size; // Declare an array of size 50 and a variable for the size of the array
    cout << "Enter number of terms : "; // Prompt the user to enter the number of elements
    cin >> size; // Store the number of elements in the size variable

    create_arr(arr, size); // Call the function to create the array

    bubble_sort(arr, size); // Call the function to sort the array

    return 0; // Return 0 to indicate successful execution
}