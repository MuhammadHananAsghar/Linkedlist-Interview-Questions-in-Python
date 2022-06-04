# MOve a last element to the front of a linkedlist
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

    
    def moveLtoF(self):
        node = self.head
        while node.next is not None:
            node = node.next
        
        temp = self.head.value
        self.head.value = node.value
        node.value = temp

linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.printLinkedList()
linkedList.moveLtoF()
linkedList.printLinkedList()
