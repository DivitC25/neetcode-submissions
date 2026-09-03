import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSearchK = max(piles)

        searchSpace = range(1, maxSearchK + 1)

        start = 0
        end = len(searchSpace) - 1

        answer = maxSearchK

        while start <= end:
            m = start + (end - start) // 2
            k = searchSpace[m]

            totalHours = sum(
                math.ceil(pile / k)
                for pile in piles
            )

            if totalHours > h:
                # k is too slow
                start = m + 1
            else:
                # k works, but maybe a smaller k works
                answer = k
                end = m - 1

        return answer


        
        