class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None


class LinkedList:
    def __init__(self):
        self.end = None

    def push(self, data):
        new_node = Node(data)
        if self.end is None:
            self.end = new_node
        else:
            temp = self.end
            while temp.nref:
                temp = temp.nref
            temp.nref = new_node

    def get(self, index):
        if index < 0:
            return None
        
        temp = self.end
        count = 0
        while temp:
            if count == index:
                return temp.data
            temp = temp.nref
            count += 1
        return None

    def remove(self, index):
        if index < 0 or self.end is None:
            return
        if index == 0:
            self.end = self.end.nref
            return

        temp = self.end
        pref = None
        count = 0
        while temp and count != index:
            pref = temp
            temp = temp.nref
            count += 1
        if temp:
            pref.nref = temp.nref

    def insert(self, index, data):
        if index < 0:
            return

        new_node = Node(data)
        if index == 0:
            new_node.nref = self.end
            self.end = new_node
        else:
            temp = self.end
            pref = None
            count = 0
            while temp and count != index:
                pref = temp
                temp = temp.nref
                count += 1
            if pref:
                pref.nref = new_node
                new_node.nref = temp

    def __iter__(self):
        temp = self.end
        while temp:
            yield temp.data
            temp = temp.nref


list1 = LinkedList()
list1.push(10)
list1.push(20)
list1.push(30)
list1.push(40)
print(list(list1))
print(list1.get(2))
list1.remove(1)
print(list(list1))
list1.insert(1, 50)
print(list(list1))