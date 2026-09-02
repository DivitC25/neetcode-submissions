class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for c in s:
            print(stack)
            if c in bracketPairs.keys():
                stack.append(c)
            else:
                if len(stack) == 0 or c != bracketPairs[stack[-1]]:
                    return False
                else:
                    stack.pop()
        
        if len(stack) > 0:
            return False
        else:
            return True
