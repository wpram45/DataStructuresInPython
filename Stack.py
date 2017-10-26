class Stack:

    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,data):
        self.items.append(data)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

n_Stack=Stack()

n_Stack.push(10)
n_Stack.push(60)
n_Stack.push(80)
n_Stack.push(30)
print("Size:",n_Stack.size())

print(n_Stack.pop())
print(n_Stack.pop())
print(n_Stack.pop())
print(n_Stack.pop())

