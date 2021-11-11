"""
Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1.

 
Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
                step by step sum
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

Example 3:
Input: nums = [1,-2,-3]
Output: 5
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""

# Solution
"""
We need to find a start value that needs to be big enough so that for any number in the input array the sum of the start value and all further numbers up to that number is at least one. To find such a number we need to sum up all the numbers and at each step check if the current prefix sum is a new minimum. Our start value needs to make up for that minimum prefix sum and we also need to add one so we are at least at 1 (start_value = -min_prefix_sum + 1).
"""
import itertools
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        #find prefix sum
        return 1-min(0,min(itertools.accumulate(nums)))
