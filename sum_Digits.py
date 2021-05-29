def sum_Digits(n):
    return 0 if n==0 else int(n%10)+sum_Digits(n//10)

t=int(input()) #no. of testcases
while t>0:
    a=int(input())
    print(sum_Digits(a))
    t-=1