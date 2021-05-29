#include<stdio.h>
#include<limits.h>

void findMinAndMax(int arr[], int low, int high, int min, int max)
{
 
    if (low == high)
    {
        if (max < arr[low]) {
            max = arr[low];
        }
 
        if (min > arr[high]) {
            min = arr[high];
        }
 
        return;
    }
 
    // if the array contains only two elements
 
    if (high - low == 1)
    {
        if (arr[low] < arr[high])       // comparison 1
        {
            if (min > arr[low]) {       // comparison 2
                min = arr[low];
            }
 
            if (max < arr[high]) {      // comparison 3
                max = arr[high];
            }
        }
        else {
            if (min > arr[high]) {      // comparison 2
                min = arr[high];
            }
 
            if (max < arr[low]) {       // comparison 3
                max = arr[low];
            }
        }
        return;
    }
    int mid = (low + high) / 2;
    findMinAndMax(arr, low, mid, min, max);
    findMinAndMax(arr, mid + 1, high, min, max);
}

int main()
{
    int arr[] = { 7, 2, 9, 3, 1, 6, 7, 8, 4 };
    int n = sizeof(arr) / sizeof(arr[0]);
    int max = INT_MIN, min = INT_MAX;
    findMinAndMax(arr, 0, n - 1, min, max);
    printf("The minimum array element is %d",min);
    printf("The maximum array element is %d",max);
    return 0;
}