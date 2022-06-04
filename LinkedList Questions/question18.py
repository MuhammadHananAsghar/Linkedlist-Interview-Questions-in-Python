# Swap Two Nodes Without Swapping Data
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

    def swapNodes(self, x, y):
        nodeX = self.head
        prevX = None
        if x == y:
            return
        
        while nodeX and (nodeX.value != x):
            prevX = nodeX
            nodeX = nodeX.next

        nodeY = self.head
        prevY = None
        while nodeY and (nodeY.value != y):
            prevY = nodeY
            nodeY = nodeY.next

        if (nodeX is None) or (nodeY is None):
            return

        if prevX is not None:
            prevX.next = nodeY
        else:
            self.head = nodeY
        
        if prevY is not None:
            prevY.next = nodeX
        else:
            self.head = nodeX

        
        temp = nodeY.next
        nodeY.next = nodeX.next
        nodeX.next = temp



linkedList = LinkedList()
linkedList.add(10)
linkedList.add(15)
linkedList.add(12)
linkedList.add(13)
linkedList.add(20)
linkedList.add(14)
linkedList.printLinkedList()
# x = 12, y = 20
linkedList.swapNodes(10, 14)
linkedList.printLinkedList()