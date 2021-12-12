"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

# Solution

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        t=sum(nums)
        if t%2==1:
            return False
        p=t//2
        dp=[False]*(p+1)
        dp[0]=True
        for i in nums:
            for j in range(p,i-1,-1):
                dp[j] = dp[j] or dp[j-i]
        return dp[-1]
