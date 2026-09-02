class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            if len(stack) == 0 or temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i))
            else:
                while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                    popped = stack.pop()
                    result[popped[1]] = i - popped[1]
                stack.append((temperatures[i], i))

        return result

        