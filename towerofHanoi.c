#include<stdio.h>
void towerOfHanoi(int n, char frod, char trod, char arod, int x)
{
    if (n == 1)
    {
        printf("\n Move disk 1 from rod %c to rod %c", frod, trod);
        return;
    }
    x++;
    towerOfHanoi(n-1, frod, arod, trod,x);
    printf("\n Move disk %d from rod %c to rod %c", n, frod, trod);
    towerOfHanoi(n-1, arod, trod, frod,x);
}
int main()
{
    printf("A is source, B is temp, C is destination\n");
    int x=0;
    int n;
    printf("Enter no. of disks:- ");
    scanf("%d",&n);
    towerOfHanoi(n, 'A', 'C', 'B',x);
    return 0;
}