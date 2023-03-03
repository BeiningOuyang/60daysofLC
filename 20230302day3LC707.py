#  Didnt pass need to reviewed, need to rewrite 20230302
class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        cur = self.head

        while index:
            cur = cur.next
            index -= 1
        return cur.val



    def addAtHead(self, val: int) -> None:

        # new = Node(val)

        # new.next = self.head
        # self.head = new

        # self.size += 1

        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:

        # new = Node(val)
        # cur = self.head

        # while cur.next:
        #     cur = cur.next

        # cur.next = new
        # self.size += 1
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:

        # if index > self.size:
        #     return
        # if index <= 0:
        #     self.addAtHead(val)
        #     return
        # cur = self.head
        # index -= 1
        # while index:
        #     cur = cur.next
        #     index -= 1
        # new = Node(val)
        # cur.next = new
        # new.next = cur.next
        # self.size += 1



        if index > self.size:
            return

        current = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # if index >= self.size or index < 0:
        #     return
        # if index == 0:
        #     self.head = self.head.next
        #     return

        # cur = self.head
        # index -= 1
        # while index:
        #     cur = cur.next
        # cur.next = cur.next.next
        # self.size -= 1

        if index < 0 or index >= self.size:
            return

        current = self.head

        if index == 0:
            self.head = self.head.next
        else:
            for _ in range(0, index - 1):
                current = current.next
            current.next = current.next.next

        self.size -= 1







# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)