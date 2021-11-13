"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

# Solution
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        # TC= O(N^2) where N no. of datas -> T.L.E
        """
		n=len(temp)
        answer=[0]*n
        for day in range(n):
            for f_day in range(day+1,n):
                if temp[f_day] > temp[day]:
                    answer[day] = f_day-day
                    break
        return answer
        """
        
        """ Create a monotonic stack -> its a stack that follows either increasing order or decreasinfg order. If any element that doesn't follow the trend (the will be peeked as its a stack), they will be popped out"""
        # TC= O(N) where N no. of datas
        n=len(temp)
        answer=[0]*n
        stack=[]
        for day, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                prev_day =stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
        return answer
