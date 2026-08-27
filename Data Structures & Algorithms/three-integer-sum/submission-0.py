class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        returnSet = set()
        for i in range(len(nums)):
            target = 0 - nums[i]
            seen = {}
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    unsortedList = [nums[i], nums[seen[complement]], nums[j]]
                    returnSet.add(tuple(sorted(unsortedList)))
                else:
                    seen[nums[j]] = j

        return [list(l) for l in returnSet]

            
                    
                
        