"""
Write a function to convert a given number into words.

Example 1:

Input:
N = 438237764
Output: forty three crore eighty two lakh 
thirty seven thousand seven hundred and 
sixty four
 

Example 2:

Input:
N = 1000
Output: one thousand

Your Task:
You don't need to read input or print anything. Your task is to complete the function convertToWords() which takes the integer n as input parameters and returns a string containing n in words.


Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 109 - 1

"""

# Solution
#User function Template for python3

class Solution:
    def convertToWords(self, n):
        # code here
        
        one = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", 
        "eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ",
        "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]
        
        ten = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]
        
        def numToWords(n,s):
            
            str = ""
            
            if n > 19:
                str += ten[(n // 10)] + one[(n % 10)]
            else:
                str += one[n]
                
            if n:
                str += s
                
            return str
        
        output = ""
        
        output += numToWords((n // 10000000), "crore ")
        output += numToWords(((n // 100000) % 100), "lakh ")
        output += numToWords(((n // 1000) % 100), "thousand ")
        output += numToWords(((n // 100) % 10), "hundred ")
        
        if(n > 100 and n % 100):
            output += "and "
            
        output += numToWords((n % 100), "")
        
        return output
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.convertToWords(n)
        print(ans)
        tc -= 1

# } Driver Code Ends
