"""
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:
Input: s = "banana"
Output: "ana"

Example 2:
Input: s = "abcd"
Output: ""
 

Constraints:

2 <= s.length <= 3 * 104
s consists of lowercase English letters.
"""

#Solution 
class Solution:
    def longestDupSubstring(self, s: str) -> str:
		res=''
		slide = 1
		for i in range(len(s)):
			longCommon = s[i+i+slide]
			temp = s[i+1:]
			while longCommon in temp:
				res = longCommon
				slide +=1
				longCommon = s[i:i+slide]
		return res
# See detail working visualisation in -> https://cscircles.cemc.uwaterloo.ca/visualize#
