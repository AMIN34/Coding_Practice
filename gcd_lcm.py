def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
def lcm(a,b):
    return (a/gcd(a,b))*b

t=int(input())
while(t):
    a,b=map(int,input().split())
    print(gcd(a,b),end=" ")
    print(lcm(a,b))
    t=t-1
