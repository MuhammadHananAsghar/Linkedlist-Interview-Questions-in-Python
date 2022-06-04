# Add "num" to a number represented as linked list
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

    def addNumber(self, number):
        num = []
        node = self.head
        while node is not None:
            num.append(node.value)
            node = node.next
        num = int("".join(num)) + number
        num = str(num)
        node = self.head
        i = 0
        while node is not None:
            node.value = num[i]
            node = node.next
            i += 1

linkedList = LinkedList()
linkedList.add("1")
linkedList.add("9")
linkedList.add("9")
linkedList.add("9")
linkedList.add("9")
linkedList.add("8")
linkedList.printLinkedList()
linkedList.addNumber(1)
linkedList.printLinkedList()
        
