# Find a modular node in a linkedlist
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

    def modular(self, key):
        if key <= 0 or self.head is None:
            return None
        node = self.head
        temp = None
        for index in range(1, self.num+1):
            if index%key == 0:
                temp = node.value
            node = node.next
        print(f"Modular node is {temp}.")

linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.add(6)
linkedList.add(7)
# linkedList.add(3)
# linkedList.add(7)
# linkedList.add(1)
# linkedList.add(9)
# linkedList.add(8)
linkedList.printLinkedList()
linkedList.modular(3)
        
