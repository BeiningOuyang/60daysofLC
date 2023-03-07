from typing import List
class Solution:
    def interaction(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # result = []

        # set1 = set(nums1)

        # set2 = set(nums2)

        # for i in set2:
        #     if i in set1:
        #         result.append(i)

        # return result
        set1 = set(nums1)
        set2 = set(nums2)

        dic = {}
        result = []
        for i in set1:
            dic[i] = 1
        for j in set2:
            dic[j] = dic.get(j, 0) + 1

        print(dic)
        for i in dic:
            if dic[i] > 1:
                result.append(i)
        return result

s = Solution()
print(s.interaction([1,2,3], [2,3,6]))

