from collections import Counter

class Solution:
    def decompose(self, a):
        aDec = frozenset(Counter(a).items())
        return aDec

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}

        for word in strs:
            wordDec = self.decompose(word)
            if wordDec in groupDict:
                groupDict[wordDec].append(word)
            else:
                groupDict[wordDec] = [word]
        
        return list(groupDict.values())
    