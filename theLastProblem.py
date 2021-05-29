""""Deep wants to become a 7-star coder on CodeChef. To achieve this goal, everyday, he has to solve 
as many problems as he can. But for the first time since he was new to programming, 
he wasn't able to solve a single problem and lost his confidence. 
Can you help him solve the problem so that he gets a new boost to go ahead?
In this problem, you are given a matrix that extends infinitely to the right and down, 
filled with values as shown below.

1   2   4   7 ...
3   5   8   ...
6   9   ...
10  ...

Let (x,y) denote the cell in the x-th row and y-th column. The upper-left cell (1,1) contains an 
integer 1. You begin at the cell (x1,y1) and must walk to the cell (x2,y2) by only moving right and down. 
Formally, from the cell (x,y), in one step you can move to the cell (x+1,y) or (x,y+1).

The value of a path is the sum of the values in all visited cells, including (x1,y1) and (x2,y2). 
You need to calculate the maximum possible value on the path of a path from (x1,y1) to (x2,y2).

Input
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains of a single line of input, four integers x1, y1, x2, y2.

Output
For each test case, output in a single line the maximum possible value of a path from (x1,y1) to (x2,y2).
"""

T=int(input())
ini = 1
inc2 = 2
arr = [[0 for col in range(1001)] for row in range(1001)]
for i in range(1000):
    inc = i + 1
    temp = ini
    for j in range(1000):
        arr[i][j] = temp
        temp += inc
        inc += 1
    ini += inc2
    inc2 += 1
for _ in range(T):
    x1,y1,x2,y2=list(map(int,input().split()))
    diff=(x2-x1)+1
    sum=0
    inix=x1
    for x in range(diff):
        sum+=arr[inix-1][y1-1]
        inix+=1
    inixy=y1
    for j in range(y2-y1):
        sum+=arr[inix-2][inixy]
        inixy+=1
    print(sum)
