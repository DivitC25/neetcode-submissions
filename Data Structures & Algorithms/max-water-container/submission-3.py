class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxWater = 0

        while start < end:
            currWater = (end - start) * min(heights[end], heights[start])
            maxWater = max(maxWater, currWater)
            if heights[start] > heights[end]:
                end -= 1
            elif heights[start] < heights[end]:
                start += 1
            else:
                start +=1

        return maxWater