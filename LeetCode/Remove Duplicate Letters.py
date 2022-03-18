"""
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.



Example 1:

Input: s = "bcabc"
Output: "abc"


Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 104
"""

# Solution

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lastI={}
        for i,ch in enumerate(s):
            lastI[ch]=i
        res=[]
        for i,ch in enumerate(s):
            if ch not in res:
                while res and ch<res[-1] and i<lastI[res[-1]]:
                    res.pop()
                res.append(ch)
        return ''.join(res)
