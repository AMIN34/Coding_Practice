import math
fact=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000,2432902008176640000]
def minus(n1,n2):
    num=n1[0]*n2[1]-n2[0]*n1[1]
    denom=n1[1]*n2[1]
    ansnum=num//math.gcd(num,denom)
    ansdenom=denom//math.gcd(num,denom)
    return [ansnum,ansdenom]
def add(n1,n2):
    num=n1[0]*n2[1]+n2[0]*n1[1]
    denom=n1[1]*n2[1]
    ansnum=num//math.gcd(num,denom)
    ansdenom=denom//math.gcd(num,denom)
    return [ansnum,ansdenom]
def mult(n1,n2):
    num=n1[0]*n2[0]
    denom=n1[1]*n2[1]
    ansnum=num//math.gcd(num,denom)
    ansdenom=denom//math.gcd(num,denom)
    return [ansnum,ansdenom]
def exp(n1,k):
    ans=[1,1]
    for i in range(k):
        ans=mult(ans,n1)
    return ans
def nCr(n,r):
    if n==r or r==0:
        return [1,1]
    if r==1 or r==n-1:
        return [n,1]
    num=fact[n]
    denom=fact[r]+fact[n-r]
    ansnum=num//math.gcd(num,denom)
    ansdenom=denom//math.gcd(num,denom)
    return [ansnum,ansdenom]
t=int(input())
for case in range(t):
    A,H,L1,L2,M,C=list(map(int, input().split()))
    P1,P2=0,0
    if (A+C)*M<H:
        print('RIP')
        continue
    if A*M>=H:
        P1,P2=1,1
        num=P1/(math.gcd(P1,P2))
        denom=P2/(math.gcd(P1,P2))
        print(f'{num}/{denom}')
        continue
    remain=H-(A*M)
    rla=math.ceil(remain/C)
    crf=[0,1]
    pl=[L1//math.gcd(L1,L2), L2//math.gcd(L1,L2)]
    pnl= minus([1,1],pl)
    for i in range(rla,M+1):
        cp=mult(nCr(M,i),exp(pl,i))
        cnp=exp(pnl,M-i)
        cp=mult(cp,cnp)
        crf=add(crf,cp)
    print(f'{crf[0]}/{crf[1]}')
