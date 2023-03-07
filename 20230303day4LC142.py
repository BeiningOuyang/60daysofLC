# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        if not head:
            return head

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                p1 = head
                p2 = slow
                while p1 != p2:
                    p1 = p1.next
                    p2 = p2.next
                return p1

        return None

        # if not head:
        #     return None

        # slow = head
        # fast = head

        # while fast and fast.next:
        #     #  why need fast and fast.next???
        #     slow = slow.next
        #     fast = fast.next.next
        #     if slow == fast:
        #         p = head
        #         q = slow
        #         while p!=q:
        #             p = p.next
        #             q= q.next
        #         return p

        # return None