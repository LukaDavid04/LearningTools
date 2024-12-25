class simpleStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        self.stack.pop()

    def print(self):
        print(self.stack)

stack1 = simpleStack()
stack1.push("ajde")
stack1.push(123)
stack1.pop()
stack1.print()