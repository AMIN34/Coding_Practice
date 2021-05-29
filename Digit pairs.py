def large(num):
  nums=str(num)
  i=9
  while i>=0:
    if str(i) in nums:
      return i
    i-=1
def small(num):
  nums=str(num)
  i=0
  while i<=9:
    if str(i) in nums:
      return i
    i+=1
def pairs(num):
  if num==2:
    return 1
  if num>=3:
    return 2
  return 0
t=int(input())
for c in range(t):
  n=int(input())
  numb=list(map(int, input(),split()))
  assert(len(numb)==n)
  bitscore=['']*n
  for i in range(len(bitscore)):
    cs=str(11*large(numb[i])+7*small(numb[i]))
    if len(cs)>2:
      cs=cs[-2:]
    bitscore[i]=cs
  oddps=[0]*10
  eveps=[0]*10
  for i in range(len(bitscore)):
    index=int(bitscore[i][0])
    if (i+1)%2==0:
      eveps[index]+=1
    else:
      oddps[index]+=1
  countpairs=[0]*10
  for i in range(10):
    if eveps[i]<=1 and oddps<=1:
      continue
    countpairs[i]+=pairs(eveps[i])+pairs(oddps[i])
    countpairs[i]=min(2,countpairs[i])
    print(sum(countpairs))