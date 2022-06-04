# Sort LinkedList on actual values which is already sorted on absolute values
class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.num = 0

    def add(self, value):
        node = Node(value)
        self.num += 1
        if self.head is None:
            self.head = node
            return

        nNode = self.head
        while nNode.next:
            nNode = nNode.next
        nNode.next = node

    def printLinkedList(self) -> None:
        node = self.head
        while node is not None:
            print(f"{node.value}",end=" -> ")
            node = node.next
        print("None")

    def sort(self):
        for _ in range(self.num):
            prev = self.head
            curr = self.head.next
            while curr is not None:
                if prev.value > curr.value:
                    temp = prev.value
                    prev.value = curr.value
                    curr.value = temp
                curr = curr.next
                prev = prev.next



linkedList = LinkedList()
linkedList.add(1)
linkedList.add(-2)
linkedList.add(-3)
linkedList.add(4)
linkedList.add(-5)
linkedList.printLinkedList()
linkedList.sort()
linkedList.printLinkedList()        
