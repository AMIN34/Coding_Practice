"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1,ls2=len(s1),len(s2)
        if ls1>ls2:
            return False
        x = ord('a')
        s1_map=[0]*26
        s2_map=[0]*26
        for i in range(ls1):
            s1_map[ord(s1[i])-x] +=1
            s2_map[ord(s2[i])-x] +=1
        for i in range(ls2-ls1):
            if s1_map==s2_map:
                return True
            s2_map[ord(s2[i + ls1]) - x] += 1
            s2_map[ord(s2[i]) - x] -= 1
        return s1_map==s2_map
