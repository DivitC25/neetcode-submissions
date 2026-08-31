class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tFreq = [0 for _ in range(58)]
        sFreq = [0 for _ in range(58)]

        for char in t:
            idx = ord(char) - ord('A')
            tFreq[idx] += 1

        start = 0
        minStart = 0
        minLength = float('inf')

        for end in range(len(s)):
            endIdx = ord(s[end]) - ord('A')
            sFreq[endIdx] += 1

            while self.freqComparator(sFreq, tFreq):
                currLength = end - start + 1

                if currLength < minLength:
                    minLength = currLength
                    minStart = start

                startIdx = ord(s[start]) - ord('A')
                sFreq[startIdx] -= 1
                start += 1

        if minLength == float('inf'):
            return ""

        return s[minStart : minStart + minLength]

    def freqComparator(self, wordFreq, targetFreq):
        for i in range(len(wordFreq)):
            if wordFreq[i] < targetFreq[i]:
                return False

        return True