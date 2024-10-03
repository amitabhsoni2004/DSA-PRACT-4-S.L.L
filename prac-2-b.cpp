// to perform binary search in array

#include<iostream>
using namespace std;

void create_arr(int arr[50] ,int size ,int k){
    cout<<"Enter elements now in ascending order : ";
    for(int i = 0; i < size; i++){
        cin>>arr[i];
    }
}

void bin_search(int arr[50], int size , int k , int start , int end){
    while (start <= end){
        int mid =( start + end )/2;

        if(arr[mid] == k){
            cout<<"Element found at index "<<mid;
            return;
        }
        else if(arr[mid] < k ){
            start = mid + 1;
        }
        else{
            end = mid - 1;
        }
    }
    cout<<"Element not found..";
}

int main(){
    int arr[50], size , k;

    cout<<"Enter the number of terms : ";
    cin>>size;
    create_arr(arr,size,k);

    cout<<"Enter element to find out : ";
    cin>>k;
    bin_search(arr,size,k , 0, size-1);
    return 0;
}