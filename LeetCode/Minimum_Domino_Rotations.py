"""
In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.

If it cannot be done, return -1.

 

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation: 
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as indicated by the second figure.


Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation: 
In this case, it is not possible to rotate the dominoes to make one row of values equal.
 

Constraints:

2 <= tops.length <= 2 * 104
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6
"""

# Solution

"""
One observation is that, if A[0] works, no need to check B[0].
Because if both A[0] and B[0] exist in all dominoes, when you swap A[0] in a whole row, you will swap B[0] in a whole at the same time.
The result of trying A[0] and B[0] will be the same.


Count the occurrence of all numbers in A and B,and also the number of domino with two same numbers.

Try all possibilities from 1 to 6.
If we can make number i in a whole row, it should satisfy that countA[i] + countB[i] - same[i] = n

Take example of
A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]

countA[2] = 4, as A[0] = A[2] = A[4] = A[5] = 2
countB[2] = 3, as B[1] = B[3] = B[5] = 2
same[2] = 1, as A[5] = B[5] = 2

We have countA[2] + countB[2] - same[2] = 6,
so we can make 2 in a whole row.

Time O(N), Space O(1)
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for i in [tops[0],bottoms[0]]:
            if all(i in d for d in zip(tops,bottoms)):
                return len(tops)-max(tops.count(i),bottoms.count(i))
        return -1
