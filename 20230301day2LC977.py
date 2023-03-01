
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        l = [0] * len(nums)
        pointer = len(nums) - 1

        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left]**2 >= nums[right]**2:
                l[pointer] = nums[left]**2
                pointer -= 1
                left += 1
            else:
                l[pointer] = nums[right]**2
                pointer -=1
                right -= 1

        return l

case1 = Solution()
l = [-4,-1,0,3,10]
print(case1.sortedSquares(l))
