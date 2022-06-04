# Sort a linkedlist of 0s, 1s and 2s

# Input 2, 1, 2, 1, 1, 2, 0, 1, 0
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
            print(f"{node.value}",end=" -> ")
            node = node.next
        print("None")

    def rearrange(self):
        node = self.head
        zeros, ones, twos = [], [], [] 
        while node is not None:
            if node.value == 0:
                zeros.append(node.value)
            if node.value == 1:
                ones.append(node.value)
            if node.value == 2:
                twos.append(node.value)
            node = node.next
        dt = zeros+ones+twos
        node, id = self.head, 0
        while node is not None:
            node.value = dt[id]
            node = node.next
            id += 1


linkedList = LinkedList()
linkedList.add(2)
linkedList.add(1)
linkedList.add(2)
linkedList.add(1)
linkedList.add(1)
linkedList.add(2)
linkedList.add(0)
linkedList.add(1)
linkedList.add(0)
linkedList.printLinkedList()
linkedList.rearrange()
linkedList.printLinkedList()

        
