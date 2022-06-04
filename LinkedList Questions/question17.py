# Print Reverse LinkedList
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

    def reversePrint(self, node):
        if node is None:
            return
        self.reversePrint(node.next)

        print(node.value, end=" ")


linkedList = LinkedList()
linkedList.add("1")
linkedList.add("10")
linkedList.add("30")
linkedList.add("14")
linkedList.printLinkedList()
linkedList.reversePrint(linkedList.head)
print()
