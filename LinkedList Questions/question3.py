# Odd and Even Positioned nodes are together in linkedlist
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
            print(node.value, end= " ")
            node = node.next
        print()

    def positioned(self):
        x = 1
        odds, evens = [], []
        node = self.head
        while node is not None:
            if x % 2 == 0:
                evens.append(node.value)
            else:
                odds.append(node.value)
            x += 1

            nums = "".join(odds+evens)
            node = node.next
        
        i = 0
        node = self.head
        while node is not None:
            node.value = nums[i]
            i += 1
            node = node.next




linkedList = LinkedList()
linkedList.add("1")
linkedList.add("2")
linkedList.add("3")
linkedList.add("4")
linkedList.add("5")
linkedList.add("6")
linkedList.add("7")
linkedList.add("8")
linkedList.printLinkedList() 
linkedList.positioned()
linkedList.printLinkedList() 


