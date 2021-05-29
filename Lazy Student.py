def multi(a,b,prime):
    ans=(a%prime * b%prime)%prime
    return ans
def ckgcd(p,q):
    while(q!=0):
        (p,q)=(q,p%q)
    return p
prime=10**9+7
max_n=1000
pascals=[[0 for i in range(max_n+1)] for j in range(max_n+1)]
pascals[0][0]=1
for i in range(1,len(pascals)):
    pascals[i][0]=1
    for j in range(1,i+1):
        pascals[i][j]=(pascals[i-1][j-1]+pascals[i-1][j])%prime
k=int(input())
for i in range(k):
    n,t,m=list(map(int, input().split()))
    if n-m<t:
        print(1)
        continue
    if n==0:
        print(0)
        continue
    
    #Finding Combination using Pascals triangle
    p=pascals[n][t]-pascals[n-m][t]
    q=pascals[n][t]
    gcd=ckgcd(p,q)
    if(gcd!=1):
        p=p//gcd
        q=q//gcd
    q_inv=pow(q,prime-2,prime)
    ans=multi(p,q_inv,prime)
    print(ans)