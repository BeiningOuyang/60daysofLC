class Solution:
    def replaceSpace(self, s: str) -> str:

        l = list(s)

        for i in range(len(l)):
            if l[i] == ' ':
                l[i] = '%20'

        return ''.join(l)