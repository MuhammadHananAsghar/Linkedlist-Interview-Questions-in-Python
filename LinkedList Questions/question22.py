# Delete Middle Node
import math

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
            print(f"{node.value}",end=" ")
            node = node.next
        print()  

    def deleteMiddle(self):
        if self.num == 1:
            self.head = None
            return
        if self.num % 2 == 0:
            mid = math.ceil(self.num/2)+1
        else:
            mid = math.ceil(self.num/2)
        mid = mid - 1
        id = 0
        temp = None
        node = self.head
        while node is not None:
            if id == mid:
                break
            temp = node
            node = node.next
            id += 1
        temp.next = temp.next.next


linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.printLinkedList()
linkedList.deleteMiddle()
linkedList.printLinkedList()
