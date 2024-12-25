class simpleStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if type(item) == int:
            self.stack.append(item)
        else:
            print("Cannot push. Simple stack only takes integers.")

    def pop(self):
        if len(self.stack) == 0:
            print("Cannot pop. Simple stack is currently empty.")
        else:
            self.stack.pop()

    def print(self):
        print(self.stack)

    def getMin(self):
        if len(self.stack) == 0:
            print("Cannot return min. Simple stack is currently empty.")
        else:
            sortedStack = self.stack.copy()
            sortedStack.sort()
            return sortedStack[0]

stack1 = simpleStack()
stack1.push(123)
print(stack1.getMin())
stack1.push(7)
print(stack1.getMin())
stack1.pop()
print(stack1.getMin())
stack1.print()