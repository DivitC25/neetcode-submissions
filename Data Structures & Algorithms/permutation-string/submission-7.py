class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        windowSize = len(s1)

        while start + windowSize - 1 < len(s2):
            subWord = s2[start : start + windowSize]
            if set(subWord) == set(s1):
                if self.wordFrequency(subWord) == self.wordFrequency(s1):
                    return True
                else:
                    start += 1
            else:
                start += 1
        
        return False
    
    def wordFrequency(self, word):
        freqMap = [0 for i in range(26)]
        for letter in word:
            idx = ord(letter) - ord('a')
            freqMap[idx] += 1
        
        return freqMap




        

            
