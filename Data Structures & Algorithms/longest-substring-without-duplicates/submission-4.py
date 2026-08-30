class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        start = 0
        end = 1
        seen = set()
        seen.add(s[start])
        longestSeq = 1

        while end < len(s):
            if s[end] not in seen:
                seen.add(s[end])
                longestSeq = max(longestSeq, end - start + 1)
                end += 1
            else:
                while s[end] in seen:
                    seen.remove(s[start])
                    start += 1
                seen.add(s[end])
                end = end + 1
        
        return longestSeq
            





        