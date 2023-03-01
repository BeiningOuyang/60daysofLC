# 704 Binary Search

from typing import List
class Solution:
    def search (self, nums: List[int], target:int ) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) -1

        while left + 1 < right:
            mid = (left + right) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1

case1 = Solution()
l = [-1,0,3,5,9,12]
t = -1
print(case1.search(l,t))


