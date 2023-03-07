from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                p1 = j + 1
                p2 = len(nums) - 1
                while p1 < p2:
                    if nums[i] + nums[j] + nums[p1] + nums[p2] == target:
                        res.append([nums[i], nums[j], nums[p1], nums[p2]])
                        p1 += 1
                        p2 -= 1
                        while p1 < p2 and nums[p1] == nums[p1 - 1]:
                            p1 += 1

                    elif nums[i] + nums[j] + nums[p1] + nums[p2] > target:
                        p2 -= 1
                    else:
                        p1 += 1