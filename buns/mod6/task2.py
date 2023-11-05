class DoubleElement:
    def __init__(self, *lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration
        pair = (self.lst[self.index], None)
        self.index += 1
        if self.index < len(self.lst):
            pair = (self.lst[self.index - 1], self.lst[self.index])
            self.index += 1
        return pair

dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)
print()

dL = DoubleElement(1, 2, 3, 4, 5)
for pair in dL:
    print(pair)