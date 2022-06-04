# Print Alternate Nodes of LinkedList using Recursion
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
            print(f"{node.value}",end=" -> ")
            node = node.next
        print("None")

    
    def alternateNodes(self, node):
        if node is None:
            return
        print(node.value, end=" -> ")
        return self.alternateNodes(node.next.next)


linkedList = LinkedList()
linkedList.add("1")
linkedList.add("2")
linkedList.add("3")
linkedList.add("4")
linkedList.add("5")
linkedList.add("6")
linkedList.add("7")
linkedList.add("8")
linkedList.add("9")
linkedList.add("10")
linkedList.alternateNodes(linkedList.head)
print('None')
linkedList.printLinkedList()
        
