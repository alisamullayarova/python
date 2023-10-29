

class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class Queue:
    def __init__(self):
        self.start = None
        self.end = None

    def pop(self):
        if self.start is None:
            return None
        val = self.start.data
        self.start = self.start.nref
        if self.start is None:
            self.end = None
        else:
            self.start.pref = None
        return val

    def push(self, val):
        new_node = Node(val)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end
            self.end.nref = new_node
            self.end = new_node

    def insert(self, n, val):
        new_node = Node(val)
        if n == 0:
            new_node.nref = self.start
            self.start.pref = new_node
            self.start = new_node
        else:
            temp = self.start
            for i in range(n - 1):
                if temp is None:
                    return
                temp = temp.nref
            if temp is None:
                return
            new_node.nref = temp.nref
            new_node.pref = temp
            if temp.nref is not None:
                temp.nref.pref = new_node
            temp.nref = new_node

    def print(self):
        temp = self.start
        while temp is not None:
            print(temp.data)
            temp = temp.nref

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
queue.insert(1, 4)
queue.pop()
queue.print()
