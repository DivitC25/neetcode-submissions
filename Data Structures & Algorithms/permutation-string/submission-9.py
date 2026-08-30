class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0 for _ in range(26)]
        targetFreq = [0 for _ in range(26)]
        windowSize = len(s1)

        if len(s2) < len(s1):
            return False

        for i in range(windowSize):
            idx = ord(s2[i]) - ord('a')
            targetIdx = ord(s1[i]) - ord('a')
            freq[idx] += 1
            targetFreq[targetIdx] += 1
        
        if freq == targetFreq:
            return True

        for i in range(len(s2) - windowSize + 1):
            if freq == targetFreq:
                return True
            else:
                startIdx = ord(s2[i]) - ord('a')
                freq[startIdx] -= 1
                if i + windowSize < len(s2):
                    endIdx = ord(s2[i + windowSize]) - ord('a')
                    freq[endIdx] += 1
        
        return False




        

            
