class StackList:

    class Knoop:
        def __init__(self, data=None, volgende=None):
            self.data = data
            self.volgende = volgende

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        hulp = self.Knoop()
        hulp.data = data
        hulp.volgende = self.top
        self.top = hulp

    def peek(self):
        return self.top.data

    def pop(self):
        hulp = self.top.data
        self.top = self.top.volgende
        return hulp
        
stack_a = StackList()
print(stack_a.is_empty())
stack_a.push('A')
stack_a.push('B')
stack_a.push('C')
print(stack_a.pop())
print(stack_a.peek())
    