"""
Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1
 

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
digits is sorted in non-decreasing order.
1 <= n <= 109
"""

# Solution

"""
1. N has n digits, so all numbers less than n digits are valid, which are: sum(len(D) ** i for i in range(1, n))

2. The loop is to deal with all numbers with n digits, considering from N[0], N[1] back to N[n-1]. For example, N[0] is valid only for c in D if c <= N[0]. If c < N[0], then N[1], ..., N[n-1] can take any number in D but if c == N[0], then we need consider N[1], and the iteration repeats. That's why if N[i] not in D, then we don't need to repeat the loop anymore.

3. Finally i==n is addressed at the end when there exists all c in D that matches N
"""
class Solution:
    def atMostNGivenDigitSet(self, D: List[str], N: int) -> int:
        N = str(N)
        n = len(N)
        res = sum(len(D) ** i for i in range(1, n))
        i = 0
        while i < len(N):
            res += sum(c < N[i] for c in D) * (len(D) ** (n - i - 1))
            if N[i] not in D: break
            i += 1
        return res + (i == n)
