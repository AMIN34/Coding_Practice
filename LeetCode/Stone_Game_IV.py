"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.


Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).


Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 105
"""

# Solution
"""
Let dp[i] represents the result of the game with i stones. dp[i]==True means the current player must win, and dp[i]==False means the current player must lose, when both players play optimally.

The next step is to find out how to calculate dp[i].

We can iterate all possible movements, and check if we can move to a False state. If we can, then we found a must-win strategy, otherwise, we must lose since the opponent has a must-win strategy in this case.

More clearly, we can iterate k from 0 and check if there exists dp[i - k*k]==False. Of course, i - k*k >= 0.

Finally, we only need to return dp[n].
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp=[False]*(n+1)
        for i in range(1,n+1):
            for k in range(1,int(i**0.5)+1):
                if dp[i-k*k]==False:
                    dp[i]=True
                    break
        return dp[n]
