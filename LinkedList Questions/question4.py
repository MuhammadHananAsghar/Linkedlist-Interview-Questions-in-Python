# Decimal Equivalent of Binary Linked List
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

    def binaryToDecimal(self, binary):
     
        decimal, i = 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        
        return decimal  

    def printLinkedList(self) -> None:
        node = self.head
        while node is not None:
            print(node.value, end= " ")
            node = node.next
        print()
    
    def BinToDec(self):
        binary = []
        decimal = 0
        if self.head is None:
            decimal = 0
            return decimal
        node = self.head
        while node is not None:
            binary.append(node.value)
            node = node.next

        binary = int("".join(binary))
        decimal = self.binaryToDecimal(binary)
        print(f"Decimal of {binary} is {decimal}.")






linkedList = LinkedList()
linkedList.add("1")
linkedList.add("0")
linkedList.add("0")
# linkedList.add("1")
# linkedList.add("1")
# linkedList.add("0")
# linkedList.add("0")
# linkedList.add("1")
# linkedList.add("0")
linkedList.printLinkedList() 
linkedList.BinToDec()

