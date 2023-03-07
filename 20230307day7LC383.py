class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        dic = {}

        for i in magazine:
            dic[i] = dic.get(i, 0) + 1

        print(dic)

        for i in ransomNote:
            if i in dic and dic[i] > 0:
                dic[i] -= 1
            else:
                return False

        return True