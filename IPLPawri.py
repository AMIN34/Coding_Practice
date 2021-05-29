t=int(input())
while(t):
    x=int(input())
    l=list(int(i) for i in input().split())[:x]
    d={}
    x=0
    for i in l:
        d[i] = d.get(i, 0) + 1
    for v,k in d.items():
        if k==3:
            x=3*v
    print(x)
    t-=1