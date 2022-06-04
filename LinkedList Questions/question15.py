# Check if LinkedList in Circular LinkedList
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
        
        temp = self.head
        node.next = self.head
        
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
        else:
            node.next = node
        
        self.head = node

    # def add(self, value):
    #     node = Node(value)
    #     if self.head is None:
    #         self.head = node
    #         return

    #     nNode = self.head
    #     while nNode.next:
    #         nNode = nNode.next
    #     nNode.next = node

    def printLinkedList(self) -> None:
        node = self.head
        if self.head is not None:
            while True:
                print(node.value, end= " ")
                node = node.next
                if node == self.head:
                    break
        print()
    
    # def printLinkedList(self) -> None:
    #     node = self.head
    #     while node is not None:
    #         print(f"{node.value}",end=" ")
    #         node = node.next
    #     print()

    def checkCircular(self):
        node = self.head

        if self.head is not None:
            while True:
                node = node.next
                if node == self.head:
                    print("It is Circular")
                    break

                if node is None:
                    print("It is not Circular")
                    break

        


linkedList = LinkedList()
linkedList.add("1")
linkedList.add("2")
linkedList.add("3")
linkedList.add("4")
linkedList.add("5")
linkedList.add("6")
linkedList.printLinkedList()
linkedList.checkCircular()
        
