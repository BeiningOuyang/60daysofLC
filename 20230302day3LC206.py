
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(p1, p2):
            if not p2:
                return p1

            p3 = p2.next
            p2.next = p1
            return reverse(p2, p3)

        return reverse(None, head)

