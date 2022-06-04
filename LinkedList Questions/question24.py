# Find the largest and smallest element in the LinkedList
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

    def smallAndlarge(self):
        if self.head is None:
            return
        temp = []
        node = self.head
        while node is not None:
            temp.append(node.value)
            node = node.next

        print(f"Maximum: {max(temp)} \nMinimum: {min(temp)}")

        


linkedList = LinkedList()
linkedList.add(43)
linkedList.add(13)
linkedList.add(54)
linkedList.add(68)
linkedList.add(23)
linkedList.add(25)
linkedList.add(20)
linkedList.printLinkedList()
linkedList.smallAndlarge()
