"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.


Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""


# Solution
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        ## RC ##
        ## APPRAOCH : BFS ##
        #   why BFS ? : we are trying to search for shortest path.
        
		## TIME COMPLEXITY : O(M^2xN) ##    (M- length of words, N - number of words)
		## SPACE COMPLEXITY : O(M^2xN) ##
        
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        size = len(beginWord)
        lookup = defaultdict(list)                                  
        for word in wordList:                                       # every word is taken from wordList
            for i in range(size):
                lookup[word[:i] + "*" + word[i+1:]].append(word)    # create every possible combination Pattern and that word can be transformed to and put into hashmap. ( include the current word aswell in the possible transformed sequence.)
                                                                    # *it =>hit, h*t => hit, hi* => hit.
                
                                                                    
        queue =  collections.deque([(beginWord, 1)])                # keeping track of path length as well. (start with 1)
        visited = {beginWord: True}
        
        while(queue):
            currWord, pathLength = queue.popleft()
            
            for i in range(size):
                possibleWordPattern = currWord[:i] + "*" + currWord[i+1:]
                
                for word in lookup[possibleWordPattern]:            # check for all words for the pattern matched.
                    if(currWord == word):
                        continue
                    
                    if(word == endWord):
                        return pathLength + 1
                    
                    if(word not in visited):
                        visited[word] = True
                        queue.append((word, pathLength + 1))
        return 0
