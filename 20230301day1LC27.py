from typing import List

class Solution:
    def removeElement(self, nums: List[int], val:int) -> int:

        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] == val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow

case1 = Solution()
l = [3,2,2,3]
v = 1
print(case1.removeElement(l,v))


