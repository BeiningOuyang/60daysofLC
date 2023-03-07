from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        size = 0

        while p1:
            size += 1
            p1 = p1.next

        l = size - n

        dummy = ListNode
        dummy.next = head
        pointer = dummy

        while l:
            pointer = pointer.next
            l -= 1

            # if pointer.next.next:
        pointer.next = pointer.next.next
        # else:
        #     pointer.next = None
        return dummy.next