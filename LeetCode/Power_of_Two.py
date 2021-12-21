"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Example 4:
Input: n = 4
Output: true

Example 5:
Input: n = 5
Output: false
 
Constraints:
-231 <= n <= 231 - 1
 
Follow up: Could you solve it without loops/recursion?
"""

# Method 1) Bit Manipulation
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and (n & (n-1))==0:
		return True
        return False

# Method 2) Recursion
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
		return True
        elif n%2!=0 and n>0:
		return False
	return self.isPowerofTwo(n/2)
