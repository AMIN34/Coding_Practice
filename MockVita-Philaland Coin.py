import math
T=int(input())
lst=list()
for i in range(T):
  j=input()
  lst.append(j)
for i in lst:
  i=int(i)
  n=int(math.log(i,2)) + 1
  print(n)