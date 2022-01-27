"""
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

 
Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.

Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 

Constraints:

1 <= nums.length <= 2 * 105
0 <= nums[i] <= 231 - 1
"""

# Solution
"""
The key idea is just build the maximal answer bit by bit, so that we want to add a '1' to every bit, but without changing the previous bits.
By using XOR, how do we get 1: just find two numbers, one has a 1 on this bit, the other has 0 (or they are opposite on this bit).
How do we guarantee that these two numbers are exactly the same two who construct the previous part of this answer? If we denote the two numbers as a and b, then the previous answer shall be a^b. We also know a and b should exist in the set prefix, and a^b^a=b. The next part is fairly simple: using just try answer ^ a for all a in prefix, if the result still exists in prefix, then the result must be b.

So actually this answer^1^p test two things:
	1. find the two elements in nums that constructs the previous answer
	2. check this two elements have opposite bits at current position
"""

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res=0
        for i in range(32)[::-1]:
            res<<=1
            pref = {num >> i for num in nums}
            res += any(res^1^p in pref for p in pref)
        return res
            
