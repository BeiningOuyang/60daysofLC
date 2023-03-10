class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1) == 0:
            return
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
        pop = self.q1.pop(0)
        self.q1, self.q2 = self.q2, self.q1
        return pop

    def top(self) -> int:
        if len(self.q1) == 0:
            return
        for i in range(len(self.q1) - 1):
            self.q2.append(self.q1.pop(0))
        top = self.q1.pop(0)
        self.q2.append(top)
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()