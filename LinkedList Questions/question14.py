# Find length of loop in LinkedList
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
        self.num = self.num + 1
        if self.head is None:
            self.head = node
            return

        nNode = self.head
        while nNode.next:
            nNode = nNode.next
        nNode.next = node

    def printLinkedList(self) -> None:
        node = self.head
        for _ in range(self.num):
            print(node.value, end= " ")
            node = node.next
        print()

    def addLoopAt_K(self, k):
        i = 1
        node = self.head
        while node.next is not None:
            if i == k:
                temp = node
            i += 1
            node = node.next
        node.next = temp

    def loopLength(self, start):
        count = 1 
        temp = start
        while start.next != temp:
            # print(start.next.value, temp.value)
            count += 1
            start = start.next        
        print(f"Length of Loop is {count}.")

    def checkLoop(self):
        slow, fast = self.head, self.head

        while slow and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                self.loopLength(slow)
                break


linkedList = LinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)
linkedList.add(5)
linkedList.add(6)
linkedList.add(7)
linkedList.printLinkedList()
linkedList.addLoopAt_K(4)
linkedList.printLinkedList()
linkedList.checkLoop()