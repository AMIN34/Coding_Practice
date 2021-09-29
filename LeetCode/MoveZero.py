# Question

"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array."""

#Method 1)
nums.sort(key = lambda x: x==0)

#Method 2)
for i in range(len(nums)):
	if nums[i] == 0:   #check if the number is zero (if yes)
		nums.append(0) #add zero to the end of the list
        nums.remove(0) #remove the first zero found (from left)
