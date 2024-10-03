// to perform linear search in 1D array

#include<iostream> // Include the iostream library for input and output

using namespace std; // Use the standard namespace

// Function to create an array by taking input from the user
void create_arr(int arr[50], int size){
    cout<<"Enter elements in array : "; // Prompt user to enter elements
    for(int i = 0; i<size; i++){ // Loop through the array
        cin >> arr[i]; // Take input for each element
    }
    // for(int i = 0; i<size; i++){
    //     cout << arr[i];
    // }
}

// Function to find an element in the array
void find_elem(int arr[50], int size , int k){
    bool found = false; // Flag to check if element is found
    for(int i = 0; i < size; i++){ // Loop through the array
        if (arr[i] == k){ // Check if current element is the one we are looking for
            cout<<"Element found at index : "<<i; // Print the index if element is found
            found = true; // Set the flag to true
            break; // Exit the loop
        }
    }
    if (!found) { // If element is not found
        cout<<"Element not found in array"; // Print not found message
    }
}

int main(){
    int arr[50] , size , k; // Declare array and variables for size and element to find
    cout<<"Enter number of terms : "; // Prompt user to enter the number of elements
    cin>> size; // Take input for the number of elements

    create_arr(arr,size); // Call function to create the array

    cout<<"Enter element to find in an Array : "; // Prompt user to enter the element to find
    cin>>k; // Take input for the element to find

    find_elem(arr,size,k); // Call function to find the element

    return 0; // Return 0 to indicate successful execution
}