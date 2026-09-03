import math

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        oneD = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                oneD.append(matrix[i][j])

        start = 0
        end = (len(matrix)*len(matrix[0])) - 1
        m = math.floor(len(matrix)*len(matrix[0])/2)

        while start <= end:
            if target < oneD[m]:
                end = m - 1
                m = start + math.floor((end - start + 1) / 2)
            elif target > oneD[m]:
                start = m + 1
                m = start + math.floor((end - start + 1) / 2)
            else:
                return True

        return False