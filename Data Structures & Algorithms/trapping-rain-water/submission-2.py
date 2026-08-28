class Solution:
    def trap(self, height: List[int]) -> int:
        leftWall = 0
        rightWall = 1
        water = 0
        waterOn = False

        if len(height) <= 2:
            return 0
        
        # Precompute the maximum height to the right to avoid O(N^2) complexity
        max_to_right = [0] * len(height)
        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_to_right[i] = current_max
            current_max = max(current_max, height[i])

        while rightWall < len(height):
            if waterOn:
                if height[rightWall] < height[leftWall] and max_to_right[rightWall-1] > height[rightWall]:
                    rightWall += 1
                else:
                    subWater = height[leftWall + 1 : rightWall]
                    water += sum([max(0, min(height[leftWall], height[rightWall]) - drop) for drop in subWater])
                    waterOn = False
                    leftWall = rightWall
                    rightWall += 1

            else:
                if height[rightWall] < height[leftWall]:
                    waterOn = True
                    rightWall += 1
                else:
                    leftWall += 1
                    rightWall += 1
        
        return water
