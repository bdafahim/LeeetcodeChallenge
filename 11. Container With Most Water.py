from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) -1
        
        while(left<right):
            curArea = min(height[left], height[right]) * (right-left)
            max_area = max(max_area, curArea)
            if(height[left] < height[right]):
                left = left + 1
            else:
                right = right -1
        
        return max_area

# Example usage:
sol = Solution()
result = sol.maxArea([2,3,4,5,18,17,6])
print(f"Output: {result}")
