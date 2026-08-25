from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in groupDict:
                groupDict[sortedWord].append(word)
            else:
                groupDict[sortedWord] = [word]
        
        return list(groupDict.values())
    