#include <stdio.h>   
int main()  
{ 
    int arr[] = {1, 2, 3, 4, 5};   //Initialize array
    int length = sizeof(arr)/sizeof(arr[0]);  //Calculate length of array arr  

    //n determine the number of times an array should be rotated  
    int n = 1;  
      
    //Displays original array  
    printf("Original array: \n");  
    for (int i = 0; i < length; i++) {   
        printf("%d ", arr[i]);   
    }   
      
    //Rotate the given array by n times toward right  
    for(int i = 0; i < n; i++){  
        int j, last;  
         
        last = arr[length-1];  //Stores the last element of the array 
      
        for(j = length-1; j > 0; j--)
            arr[j] = arr[j-1];  //Shift element of array by one    
        
        arr[0] = last;   //Last element of array will be added to the start of array. 
    }  
      
    printf("\n");  
      
    //Displays resulting array after rotation  
    printf("Array after right rotation: \n");  
    for(int i = 0; i< length; i++){  
        printf("%d ", arr[i]);  
    }  
    return 0;  
}