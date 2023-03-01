from typing import List


# sliding window
class Solution:
    def minSubarray(self, target: int, nums: List[int]) -> int:

        left = 0
        right = 0

        sum = 0
        l = len(nums) + 1

        while right < len(nums):
            sum += nums[right]
            while sum >= target:
                l = min(l, right+1-left)
                sum -= nums[left]
                left+=1
            right += 1

        if l == len(nums) + 1:
            return 0
        return l

case1 = Solution()
print(case1.minSubarray(7,[2,3,1,2,4,3]))



