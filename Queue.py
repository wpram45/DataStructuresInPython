class Queue:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q=Queue()
q.enqueue(4)
q.enqueue("hi")
q.enqueue(False)
print(q.size())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
