"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 
Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

# O(n) time
# we scan from left to right, "total" tracks the 
# sum of the subarray. If the sum is less than s,
# right moves forward one step, else left moves forward
# one step, left and right form a window.
def minSubArrayLen(self, s, nums):
    total = left = right = 0
    res = len(nums) + 1
    while right < len(nums):
        total += nums[right]
        while total >= s:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1
        right += 1
    return res if res <= len(nums) else 0


# O(nlogn)
# preSum + binary search
class Solution:
	def minSubArrayLen(self, target, nums):
		result = len(nums) + 1
		for idx, n in enumerate(nums[1:], 1):
			nums[idx] = nums[idx - 1] + n
		left = 0
		for right, n in enumerate(nums):
			if n >= target:
				left = self.find_left(left, right, nums, target, n)
				result = min(result, right - left + 1)
		return result if result <= len(nums) else 0
	
	"""
	In the regular binary search, you're searching for a single element from a list of int whereas in this case, we're looking for a difference of values in left and right 	index pointer (from mutated nums list which now has a cumulative sum from 0 to the current index) which has to be greater than or equal to the target.

	If you're thinking a regular iterative binary search below, the reason why right = mid -1 is because 1 is the case of " if target == data[mid]:" which is already checked. 		However, in the case above, you can't have something like " if target == data[mid]:" since the values in "nums" are all cumulative sums and you shouldn't do " 
	right = mid -1" or else it'll mess up the window of our search by ignoring the "1" which will be used to get the "mid" index"""
	
	def find_left(self, left, right, nums, target, n):
		while left < right:
			mid = (left + right) // 2
			if n - nums[mid] >= target:
				left = mid + 1
			else:
				right = mid
		return left
