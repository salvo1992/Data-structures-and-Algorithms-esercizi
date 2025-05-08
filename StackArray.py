class StackArray:
    def __init__(self):
        self._items = []
    
    def push(self, item):
        self._items.append(item)
    
    def is_empty(self):
        return len(self._items) == 0
    
    def pop(self):
        if not self.is_empty():
            self._items.pop()
        else:
            print("Lo stack è vuoto!")
    
    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        else:
            print("Lo stack è vuoto!")