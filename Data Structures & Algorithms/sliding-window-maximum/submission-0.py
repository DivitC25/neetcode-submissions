class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []
        
        prevMax = float("-inf")
        currMax = float("-inf")
        prevMaxIdx = -1
        resList = []

        for i in range(len(nums) - k + 1):
            if prevMaxIdx >= i and prevMaxIdx < i + k:
                currMax = max(prevMax, nums[i + k - 1])
                resList.append(currMax)
                if prevMax < nums[i + k - 1]:
                    prevMaxIdx = i + k - 1
                prevMax = currMax
            else:
                offset, currMax = max(enumerate(nums[i : i + k]), key = lambda x: x[1])
                resList.append(currMax)
                prevMax = currMax
                prevMaxIdx = i + offset
        
        return resList