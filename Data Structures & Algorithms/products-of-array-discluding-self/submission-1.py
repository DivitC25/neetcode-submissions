import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        result = []

        for num in nums:
            if num != 0 or zeroCount > 1:
                prod *= num
            else:
                zeroCount += 1
        
        for num in nums:
            if zeroCount > 1:
                result.append(0)
            elif zeroCount == 1:
                if num == 0:
                    result.append(prod)
                else:
                    result.append(0)
            else:
                result.append(prod // num)

        
        return result



        