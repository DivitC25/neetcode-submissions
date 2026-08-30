class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        windowSize = len(s1)
        setOne = set(s1)
        for i in range(len(s2) - windowSize + 1):
            subWord = s2[i : i + windowSize]
            if self.wordFrequency(subWord) == self.wordFrequency(s1):
                return True
        
        return False
    
    def wordFrequency(self, word):
        wordDict = {}
        word = ''.join(sorted(word))
        for letter in word:
            if letter in wordDict:
                wordDict[letter] += 1
            else:
                wordDict[letter] = 1
        
        return frozenset(tuple(wordDict.items()))

            
