/*Given a number N. The task is to reduce the given number N to 1 in the minimum number of steps. 
You can perform any one of the below operations in each step.

Operation 1: If the number is even then you can divide the number by 2.
Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).

You need to print the minimum number of steps required to reduce the number N to 1 by performing 
the above operations.

Example:-

Input : n = 15
Output : 5
 15 is odd 15+1=16    
 16 is even 16/2=8     
 8  is even 8/2=4 
 4  is even 4/2=2     
 2  is even 2/2=1     

Input : n = 7
Output : 4
    7->6    
    6->3 
    3->2    
    2->1

*/
/*
Method 1 – 
The idea is to recursively compute the minimum number of steps required.  
If the number is even, then we are allowed to only divide the number by 2.
But, when the number is Odd, we can either increment or decrement it by 1. So, we will use recursion 
for both n-1 and n+1 and return the one with the minimum number of operations.*/

/* #include<bits/stdc++.h>
using namespace std;

int count(int n){
    if(n==1)
        return 0;
    else if(n%2==0)
        return 1+ count(n/2);
    else
        return 1+min(count(n-1),count(n+1));
}
int main(){
    int n;
    cin>>n;
    cout<<count(n);
} */

/*
Method 2 – (Efficient Solution)
It is clear with little observation that performing an increment of 1 or a decrement of 1 on an 
odd number can result in an even number, one of it divisible by 4. For an odd number, the 
only operation possible is either an increment of 1 or a decrement of 1, most certainly one operation 
will result in a number divisible by four, this is the optimal choice clearly. 

Algorithm:-
1. Initialize count = 0
2. While number is greater than one perform following steps - 
         Perform count++ for each iteration
         if num % 2 == 0, perform division
         else if num % 4 ==1 or n==3, perform increment
         else perform decrement (as odd % 4 is either 1 or 3)
3. return count;
*/
#include<bits/stdc++.h>
using namespace std;

int countways(int n){
    int count=0;
    while(n>1){
        count++;
        if(n%2==0)
            n/=2;
        else if(n%4==1 || n==3)
            n-=1;
        else
            n+=1;
    }
    return count;
}
int main(){
    int n;
    cin>>n;
    cout<<countways(n);
}
