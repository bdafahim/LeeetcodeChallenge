from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        indices = []
        while(l<r):
            if(numbers[l] + numbers[r] == target):
                indices = [l+1,r+1]
                return indices
            if(numbers[l] + numbers[r] > target):
                r-=1
            else:
                l += 1

# Example usage:
sol = Solution()
result = sol.twoSum([2,3,4], 6)
print(f"Output: {result}")
