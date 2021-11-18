"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

# Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        res=s[0]
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
                    dp[i][j]=True
                    if j+1-i>len(res):
                        res=s[i:j+1]
        return res
