def isprime(num):
    if (num%2==0):
        return False
    if num<2:
        return False
    i=2
    while(i*i<=num):
        if (num%i==0):
            return False
        i+=1
    return True
def getprimes(start,end):
    primes_100=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
    startindx=0
    endindx=len(primes_100)-1
    while(startindx<=endindx and primes_100[startindx]<start):
        startindx+=1
    while(endindx>=startindx and primes_100[endindx]>end):
        endindx-=1
    req_lst=primes_100[startindx:endindx+1]
    return req_lst
def combination(original_list):
    combine=[]
    for i in range(len(original_list)):
        for j in range(len(original_list)):
            if i!=j:
                combined=str(original_list[i])+str(original_list[j])
                combined=int(combined)
                if isprime(combined):
                    combine.append(combined)
    combine=list(set(combine))
    return combine
def fibonaci(first,second,k):
    if k==1:
        return first
    if k==2:
        return second
    for i in range(3,k+1):
        q=first+second
        first=second
        second=q
    return q
t=int(input())
for i in range(t):
    n1,n2=list(map(int, input().split()))
    l1=getprimes(n1,n2)
    l2=combination(l1)
    a=max(l2)
    b=min(l2)
    k=len(l2)
    print(k)
    ans=fibonaci(b,a,k)
    print(ans)