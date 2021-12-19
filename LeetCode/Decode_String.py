"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

#Solution
"""
    When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
    push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
    the enclosed string k times.
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        currS=""
        k=0
        for c in s:
            if c=='[':
				# Just finished parsing this k, save current string and k for when we pop
                stack.append((currS,k))
				
				# Reset current_string and k for this new frame
                currS=""
                k=0
            elif c==']':
				# We have completed this frame, get the last current_string and k from when the frame 
            	# opened, which is the k we need to duplicate the current current_string by
                ls,lk = stack.pop(-1)
                currS=ls+lk*currS
            elif c.isdigit():
                k=k*10+int(c)
            else:
                currS+=c
        return currS
