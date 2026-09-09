class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(nums, target, sequence):
            nonlocal res
            if target == 0:
                res.append(tuple(sorted(sequence)))
            elif target < 0:
                return
            elif not nums:
                return
            else:
                helper(nums, target - nums[0], sequence + [nums[0]])
                helper(nums[1:], target, sequence)
        
        helper(nums, target, [])
        return [list(l) for l in set(res)]
        