
class Solution:
    def reverseWords(self, s: str) -> str:

        l = s.strip().split()

        print(l)


        l = l[::-1]

        res = ' '.join(l)

        return res

#
# s = 'the  sky'
# print(s)
# l = list(s)
# print(l)
#
# for i in range(len(l)):
#     if i > 0 and l[i] == ' ' and l[i-1] == " ":
#         l[i] = ''
#
# print(''.join(l))