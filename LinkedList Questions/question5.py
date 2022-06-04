# Circular LinkedList
class Node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, value):
        node = Node(value)
        
        temp = self.head
        node.next = self.head

        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        self.head = node

    def printLinkedList(self) -> None:
        node = self.head
        if self.head is not None:
            while True:
                print(node.value, end= " ")
                node = node.next
                if node == self.head:
                    break
        print()






clinkedList = CircularLinkedList()
clinkedList.add("1")
clinkedList.add("2")
clinkedList.add("3")
clinkedList.add("4")
clinkedList.add("5")
clinkedList.add("6")
clinkedList.add("7")
clinkedList.add("8")
clinkedList.add("9")
clinkedList.printLinkedList() 
