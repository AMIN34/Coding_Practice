"""
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

 

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""

# Solution

# Method 1) Using math logarithm. log(m*n) = log(m)+log(n)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k==0:
            return 0
        k = math.log(k)
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+math.log(i))
        ans=0
        for i,n in enumerate(prefix):
            j=bisect.bisect(prefix,n+k-1e-9,i+1)
            ans += j-i-1
        return ans

# Method 2) Sliding Window
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding window approach is possible because all numbers are positive. See constraints.
        if k<=1:
            return 0
        multi = 1
        res=left=0
        for right,val in enumerate(nums):
            multi *=val
            while multi>=k:
                multi /= nums[left]
                left+=1
            res += right - left + 1
        return res

