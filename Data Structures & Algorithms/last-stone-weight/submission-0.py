class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nStones = [-1 * stone for stone in stones]
        heapq.heapify(nStones)

        while len(nStones) > 0:
            if len(nStones) == 1:
                return -1 * nStones[0]
            x = -1 * heapq.heappop(nStones)
            y = -1 * heapq.heappop(nStones)

            if x > y:
                heapq.heappush(nStones, (-1 * (x - y)))
            elif y > x:
                heapq.heappush(nStones, (-1 * (y - x)))
        
        return 0
            
        