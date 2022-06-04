# Get Nth value in a linkedlist
class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, value):
        node = Node(value)
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

    def getNth(self, index):
        node = self.head
        i = 0
        while node is not None:
            if index == i:
                return f"The node at index {i} is {node.value}."
            node = node.next
            i += 1

linkedList = LinkedList()
linkedList.add("1")
linkedList.add("10")
linkedList.add("30")
linkedList.add("14")
linkedList.printLinkedList()
print(linkedList.getNth(2))
        
