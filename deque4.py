class Dequeue:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def append(self, data):
        self.items.append(data)
 
    def append_left(self, data):
        self.items.insert(0, data)
 
    def pop(self):
        return self.items.pop()
 
    def pop_left(self):
        return self.items.pop(0)
        
    def display(self):
        print(self.items)

q = Dequeue()
q.display()
q.append("a")
q.append("b")
q.append("c")
q.display()
q.append_left("d")
q.append_left("e")
q.append_left("f")
q.display()
q.pop()
q.display()
q.pop_left()
q.display()