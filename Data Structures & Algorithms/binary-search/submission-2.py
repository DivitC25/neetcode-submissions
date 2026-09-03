import math

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = math.floor(len(nums) / 2)
        start = 0
        end = len(nums) - 1


        while start <= end:
            if target < nums[m]:
                end = m - 1
                m = start + math.floor((end - start + 1) / 2)
            elif target > nums[m]:
                start = m + 1
                m = start + math.floor((end - start + 1) / 2)
            else:
                return m
        
        return -1
        



        