class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([c for c in s if c.isalnum()])
        s = s.lower()

        if s == s[::-1]:
            return True
        else:
            return False
        