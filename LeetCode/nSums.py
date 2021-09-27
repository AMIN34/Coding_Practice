def nSum(self, nums: List[int], target: int, n:int) -> List[List[int]]:
        def kSums(nums: List[int], target: int, k:int)->List[List[int]]:
            res=[]
            if len(nums)==0 or nums[0]*k > target or nums[-1]*k<target:
                return res
            if k==2:
                return twoSums(nums,target)
            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                    for subs in kSums(nums[i+1:], target - nums[i], k-1):
                        res.append([nums[i]]+subs)
            return res
        
        def twoSums(nums: List[int], target: int)->List[List[int]]:
            res=[]
            s=set()
            for i in range(len(nums)):
                if len(res) == 0 or res[-1][1]!=nums[i]:
                    if target-nums[i] in s:
                        res.append([target-nums[i],nums[i]])
                s.add(nums[i])
            return res
        nums.sort()
        return kSums(nums,target,n)
