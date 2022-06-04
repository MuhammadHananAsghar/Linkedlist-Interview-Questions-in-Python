# How many times a particular number occurs in a linkedlist
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


    def times(self, key=1):
        occurs = 0
        node = self.head
        while node is not None:
            if node.value == key:
                occurs += 1
            node = node.next
        
        print(f"{key} occurs {occurs} times in the linkedlist.")
        
        


linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(1)
linkedList.add(2)
linkedList.add(1)
linkedList.add(3)
linkedList.add(1)
linkedList.printLinkedList()
linkedList.times(2)
