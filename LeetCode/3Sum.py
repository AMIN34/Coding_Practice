"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

# Solution

# Method 1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

            # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
            if len(z) >= 3:
                res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        from itertools import combinations

        for x, y in combinations(n, 2):
            target = -1 * (x + y)
            if target in P:
                res.add(tuple(sorted([x, y, target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set

        for x, y in combinations(p, 2):
            target = -1 * (x + y)
            if target in N:
                res.add(tuple(sorted([x, y, target])))

        return [list(x) for x in res]
	
# Method 2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # 3 cases
        counter = collections.Counter(nums)
        res = []
        
        # 1. [x, x, x]
        if 0 in counter and counter[0] >= 3:
            res.append([0, 0, 0])
        
        # 2. [x, x, -2x]
        for x in counter.keys():
            if counter[x] >= 2 and counter[-2*x] >= 1 and x != 0:
                res.append([x, x, -2*x])
                
        # 3. [x, y, -x-y]
        keys = sorted(list(counter.keys()))
		# above keys will return a list with unique elements and that is sorted
        keys_set = set(keys)
        for i in range(len(keys)-1):
            for j in range(i+1, len(keys)):
                x, y = keys[i], keys[j]
                z = -x-y
                if z <= y:
                    break
                if z in keys_set:
                    res.append([x, y, z])
                    
        return res
	
# Method 3)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-1):
            target = -nums[i]
            d={}
            for ind,num in enumerate(nums[i+1:]):
                if target-num in d and [nums[i],target-num,num] not in res:
                    res.append([nums[i],target-num,num])
                else:
                    d[num]=ind
        return res
