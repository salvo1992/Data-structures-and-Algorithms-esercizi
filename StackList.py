
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def push(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node
    
    def pop(self):
        if not self.is_empty():
            self.head = self.head.next
        else:
            print("Lo stack è vuoto!")
    
    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Lo stack è vuoto!")
