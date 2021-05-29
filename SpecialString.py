"""You are given a string S and you want to make it (n,k) special.
String A is (n,k) special if after concatenating n copies of string 
A we get at least k substring of A in the resulting string (Overlapping substrings also count). 
Your task is to find the minimum number of characters you need to alter to make string S, (n,k) special.

Note : Inputs are given such that it is always possible to get at least k substrings"""

import math,sys,bisect,heapq,os
from collections import defaultdict,Counter,deque
from itertools import groupby,accumulate
from functools import lru_cache
#sys.setrecursionlimit(200000000)
pr = lambda x:	x
def input(): return sys.stdin.readline().rstrip('\r\n')
#input = iter(sys.stdin.buffer.read().decode().splitlines()).__next__
aj = lambda: list(map(int, input().split()))
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
#MOD = 1000000000 + 7
def Y(c):  print(["NO","YES"][c])
def y(c):  print(["no","yes"][c])
def Yy(c):  print(["No","Yes"][c])


def printDivisors(n) : 
    A=[] 
    i = 1
    while i <= math.sqrt(n): 
        if (n % i == 0) : 
            if (n / i == i) : 
                A.append(i) 
            else : 
                A.append(i) 
                A.append(n//i) 
        i = i + 1
    return A

def solve():
	for _ in range(int(input())):
		n,k = aj()
		s = input()
		if n >= k or k == 1 or len(set(s)) == 1:
			print(0)
		else:
			def fun(l):
				G = defaultdict(Counter)
				for i in range(len(s)):
					G[i%l][s[i]] += 1
				count = 0
				tot = len(s)//l
				# pr(G)
				# print(l)
				for i in G.keys():
					c = G[i].most_common(1)[0][1]
					count += tot - c
				return count

			ans = 1e9
			loop = (len(s)*(n-1))//(k-1)
			d= printDivisors(len(s))
			d.sort()
			for l in d:
				if l > loop:
					break
				temp = fun(l)
				ans = min(ans,temp)
			print(ans)

solve()