# Reverse each word in a linked list node
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
        print('None')

    def reverseWord(self, string):
        reverse = reversed([character for character in string])
        reverse = "".join(reverse)
        return reverse

    def reverseLinkedListNode(self):
        node = self.head
        while node is not None:
            node.value = self.reverseWord(node.value)
            node = node.next

linkedList = LinkedList()
linkedList.add("Publish")
linkedList.add("your")
linkedList.add("own")
linkedList.add("articles")
linkedList.add("on")
linkedList.add("internet")
linkedList.printLinkedList()
linkedList.reverseLinkedListNode()
linkedList.printLinkedList()
