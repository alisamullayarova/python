class Node:
    def __init__(self, data):
        self.data = data
        self.pref = None

class Stack:
    def __init__(self):
        self.end = None

    def pop(self):
        if self.end is None:
            return None
        else:
            data = self.end.data
            self.end = self.end.pref
            return data
        
    def push(self, val):
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end = new_node

    def print(self):
        temp = self.end
        while temp:
            print(temp.data, end = ' ')
            temp = temp.pref
        print()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.print()
print(stack.pop())
stack.print()
