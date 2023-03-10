class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i == '+':
                temp = stack.pop()
                sum = int(stack.pop()) + int(temp)
                stack.append(sum)

            elif i == '-':
                temp = stack.pop()
                sub = int(stack.pop()) - int(temp)
                stack.append(sub)

            elif i == '*':
                temp = stack.pop()
                mul = int(stack.pop()) * int(temp)
                stack.append(mul)

            elif i == '/':
                temp = stack.pop()
                if int(stack[-1]) // int(temp) < 0:
                    de = -(int(stack.pop()) // (-int(temp)))
                else:
                    de = int(stack.pop()) // int(temp)
                stack.append(de)

            else:
                stack.append(i)

        return int(stack.pop())