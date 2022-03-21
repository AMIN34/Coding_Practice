"""
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.


Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""

# Solution

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        rightM = {c:i for i,c in enumerate(s)}
        l=r=0
        res=[]
        for i, letter in enumerate(s):
            r = max(r,rightM[letter])
            if i==r:
                res+=[r-l+1]
                l=i+1
        return res
