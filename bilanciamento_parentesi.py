#creiamo uno stack per il controllo del bilanciamento delle parentesi di apertura e chiusura inserendo un imput 

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Lo stack è vuoto!")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Lo stack è vuoto!")


def bilanciamento_parentesi(stringa):
    stack = Stack()
    parentesi_apertura = "({["
    parentesi_chiusura = ")}]"
    mappa_parentesi = {")": "(", "}": "{", "]": "["}

    for char in stringa:
        if char in parentesi_apertura:
            stack.push(char)
        elif char in parentesi_chiusura:
            if stack.is_empty() or stack.peek() != mappa_parentesi[char]:
                print("Le parentesi non sono bilanciate!")
                return False
            else:
                stack.pop()

    if stack.is_empty():
        print("Le parentesi sono bilanciate!")
        return True
    else:
        print("Le parentesi non sono bilanciate!")
        return False

stringa = input("Inserisci una stringa: ")
bilanciamento_parentesi(stringa)    




