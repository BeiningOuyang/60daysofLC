class Solution:
    def isHappy(self, n: int) -> bool:

        strN = str(n)
        sum = 0
        hashset = set()

        while sum!= 1:
            for i in strN:
                sum = sum + int(i)*int(i)
            if sum == 1:
                return True
            if sum in hashset:
                return False
            else:
                hashset.add(sum)
            strN = str(sum)
            sum = 0
