#Leetcode Problem No. 17 letterCombinations
# Question- Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Solution(Python):-

def letterCombinations(digits):
  numLetter={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
  x=[]
  if len(digits)<1:
    return x
  digits=list(digits) #separating digits into list in order to access the hashMap
  for i in range(len(digits)):
    a=list(numLetter[digits[i]])  
    x.append(a)     #appending the values of respective keys from hashmap
  x=list(product(*x))  #creating tuples to form the letter combination
  res = [''.join(i) for i in x]  # tuptle to string and added to list. And hence the final answer.
  return res
digits=input()
print(letterCobinations(digits)
