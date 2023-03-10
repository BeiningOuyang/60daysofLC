class Solution:
    def isValid(self, s: str) -> bool:

        dic = {'(': ')', '[': ']', '{': '}'}

        stack = []

        # ({[]})

        for i in s:
            if i in dic:
                stack.append(i)
                print(i)
            else:
                if len(stack) == 0:
                    return False
                elif i == dic[stack[-1]]:
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        return False

        # l = []
        # for i in s:
        #     if i == "("  :
        #         l.append(i)
        #     elif i == ")":
        #         if len(l) > 0 and l[-1] == "(":
        #             l.pop(-1)
        #         else:
        #             return False
        #     elif i == "[":
        #         l.append(i)
        #     elif i == ']':
        #         if len(l) > 0 and l[-1] == "[":
        #             l.pop(-1)
        #         else:
        #             return False
        #     elif i == "{":
        #         l.append(i)
        #     elif i == '}':
        #         if len(l) > 0 and l[-1] == "{":
        #             l.pop(-1)
        #         else:
        #             return False

        # if len(l) == 0:
        #     return True
        # else:
        #     return False