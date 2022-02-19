"""
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 
Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.


Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.


Example 3:

Input: nums = [2,10,8]
Output: 3
 

Constraints:

n == nums.length
2 <= n <= 105
1 <= nums[i] <= 109
"""

# Solution

"""
For each a in nums,
divide a by 2 until it is an odd.
Push divided a and its original value in to the pq.

The current max value in pq is noted as ma.
We iterate from the smallest value in pq,
Update res = min(res, ma - a),
then we check we can get a * 2.

If a is an odd, we can get a * 2,
If a < a0, which is its original value, we can also get a*2.

If we can, we push [a*2,a0] back to the pq and continue this process.


Complexity
Time O(nlogn)
Space O(n)
"""

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        for a in nums:
            heapq.heappush(pq, [a / (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(nums):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return int(res)
