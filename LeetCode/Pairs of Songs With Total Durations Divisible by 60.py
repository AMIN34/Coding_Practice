"""
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500
"""

# Solution
"""
Calculate the time % 60 then it will be exactly same as two sum problem.

Explanation
t % 60 gets the remainder from 0 to 59.
We count the occurrence of each remainders in a array/hashmap c.

we want to know that, for each t,
how many x satisfy (t + x) % 60 = 0.

The straight forward idea is to take x % 60 = 60 - t % 60,
which is valid for the most cases.
But if t % 60 = 0, x % 60 = 0 instead of 60.

One solution is to use x % 60 = (60 - t % 60) % 60,
the other idea is to use x % 60 = (600 - t) % 60.
Not sure which one is more straight forward.
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = [0]*60
        res=0
        for t in time:
            res += count[-t%60]
            count[t%60]+=1
        return res
	
# python solution if you are not confident messing with math operators

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        c = [0] * 61
        for x in time:
            m = x % 60
            ans += c[60 - m]
            c[m if m else 60] += 1
        return ans
