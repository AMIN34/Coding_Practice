import math
def ckgcd(p,q):
    while(q!=0):
        (p,q)=(q,p%q)
    return p
def mulInv(a,m=1000000007):
    m0 = m 
    y = 0
    x = 1
  
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
  
        t = m 
        m = a % m 
        a = t 
        t = y 
   
        y = x - q * y 
        x = t 
    if (x < 0) : 
        x = x + m0 
  
    return x

def nCr(n,r):
    f = math.factorial
    u = f(n) / f(r) / f(n-r)
    return u
  
t=int(input())
for i in range(t):
    qb, l, c = [int(x) for x in input().split()]
    p=(nCr(qb,c))-(nCr((qb-l),c))
    q=nCr(qb,c)
    gcd=ckgcd(p,q)
    if(gcd!=1):
        p=p/gcd
        q=q/gcd
    print(int((p*mulInv(q)) % 1000000007))