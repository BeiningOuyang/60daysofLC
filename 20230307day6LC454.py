from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        hashmap = dict()

        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1 + n2] = 1
        count = 0

        for n3 in nums3:
            for n4 in nums4:
                if (0 - (n3 + n4)) in hashmap:
                    count = count + hashmap[0 - (n3 + n4)]

        return count
