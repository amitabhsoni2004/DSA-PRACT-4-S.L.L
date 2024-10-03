// perform addition, subtraction,division ,multiplication, and transpose of 2D matrix

#include<iostream> // Include the iostream library for input and output

const int rows = 2; // Define the number of rows in the matrix
const int cols = 2; // Define the number of columns in the matrix

using namespace std; // Use the standard namespace

// Function to input elements into a matrix
void input_matrix(int mat[rows][cols]){
    cout<<"Enter elements in matrix : \n";
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<cols; j++){
            cin >> mat[i][j]; // Input each element
        }
    }
}

// Function to display elements of an integer matrix
void display_matrix(int mat[rows][cols]){
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<cols; j++){
            cout << mat[i][j] << " "; // Output each element
        }
        cout<< "\n"; // New line after each row
    }    
}

// Function to display elements of a float matrix
void display_float_matrix(float mat[rows][cols]){
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<cols; j++){
            cout << mat[i][j] << " "; // Output each element
        }
        cout<< "\n"; // New line after each row
    }    
}

// Function to add two matrices
void addition(int mat1[rows][cols], int mat2[rows][cols], int result[rows][cols]){
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<cols ; j++){
            result[i][j] = mat1[i][j] + mat2[i][j]; // Add corresponding elements
        }
    }
}

// Function to subtract one matrix from another
void subtraction(int mat1[rows][cols], int mat2[rows][cols], int result[rows][cols]){
    for(int i = 0; i<rows; i++){
        for(int j = 0; j<cols ; j++){
            result[i][j] = mat1[i][j] - mat2[i][j]; // Subtract corresponding elements
        }
    }
}

// Function to divide one matrix by another
void division(int mat1[rows][cols],int mat2[rows][cols],float result1[rows][cols]){
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            if(mat2[i][j] != 0){
                result1[i][j] = mat1[i][j] / mat2[i][j]; // Divide corresponding elements
            }else{
                cout<<"Division by zero at element("<<i<<","<<j<<")\n";
                result1[i][j] = 0; // Handle division by zero
            }
        }
    }
}

// Function to multiply two matrices
void multiply(int mat1[rows][cols], int mat2[rows][cols], int result[rows][cols]){
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            result[i][j] = 0; // Initialize result element to 0
            for(int k = 0; k < cols; k++){
                result[i][j] += mat1[i][k] * mat2[k][j]; // Multiply and accumulate
            }
        }
    }
}

// Function to transpose a matrix
void transpose(int mat[rows][cols],int result[rows][cols]){
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cols; j++){
            result[i][j] = mat[j][i]; // Swap rows and columns
        }
    }
}

int main(){
    int mat1[rows][cols]; // Declare first matrix
    int mat2[rows][cols]; // Declare second matrix
    int result[rows][cols]; // Declare result matrix for integer operations
    float result1[rows][cols]; // Declare result matrix for float operations

    cout<<"Matrix 1:\n";
    input_matrix(mat1); // Input elements for first matrix

    cout<<"Matrix 2:\n";
    input_matrix(mat2); // Input elements for second matrix

    cout<<"\nMatrix1:\n";
    display_matrix(mat1); // Display first matrix

    cout<<"\nMatrix2:\n";
    display_matrix(mat2); // Display second matrix

    // Addition
    addition(mat1,mat2, result);
    cout<<"\nAddition Matrix:\n";
    display_matrix(result); // Display addition result

    // Subtraction
    subtraction(mat1,mat2, result);
    cout<<"\nSubtraction Matrix:\n";
    display_matrix(result); // Display subtraction result

    // Division
    division(mat1,mat2, result1);
    cout<<"\nDivision Matrix:\n";
    display_float_matrix(result1); // Display division result

    // Multiplication
    multiply(mat1,mat2, result);
    cout<<"\nMultiply Matrix:\n";
    display_matrix(result); // Display multiplication result

    // Transpose of mat1
    transpose(mat1,result);
    cout<<"\nTranspose of Matrix1:\n";
    display_matrix(result); // Display transpose of first matrix

    // Transpose of mat2
    transpose(mat2,result);
    cout<<"\nTranspose of Matrix1:\n";
    display_matrix(result); // Display transpose of second matrix

    return 0; // Return 0 to indicate successful execution
}
