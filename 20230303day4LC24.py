
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head:[ListNode]) -> [ListNode]:

        if not head:
            return

        dummy = ListNode()
        dummy.next = head
        pr = dummy
        p1 = head

        while p1 and p1.next:
            p2 = p1.next
            after = p2.next
            pr.next = p2
            p2.next = p1
            p1.next = after
            pr = pr.next.next
            p1 = after

        return dummy.next


c1 = Solution()

