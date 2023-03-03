class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeElement(self, head: ListNode, val: int) -> ListNode:

        if not head:
            return None

        dummy = ListNode()
        dummy.next = head
        pointer = dummy

        while pointer.next:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next

        return dummy.next

