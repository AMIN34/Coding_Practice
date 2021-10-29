"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.


Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

# Solution 
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i] != nums[i-1]:
                l=len(res)
            for j in range(len(res)-l,len(res)):
                res.append(res[j]+[nums[i]])
        return res
