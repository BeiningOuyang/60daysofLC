from typing import Optional, List
# Definition for singly-linked list.

# 另外一种方法是尾部对其

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        p1 = headA

        while p1:
            p2 = headB
            while p2:
                if p1 == p2:
                    return p1
                p2 = p2.next
            p1 = p1.next

        return None