class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for i in range(len(points)):
            x, y = points[i]
            dist = ((x**2) + (y**2))**(1/2)
            negDist = -1 * dist
            heapq.heappush(maxHeap, (negDist, i, (x, y)))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [list(element[2]) for element in maxHeap]

        