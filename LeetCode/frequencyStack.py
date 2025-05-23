class frequencyStack:
    def __init__(self):
        self.stack = []
        self.frequency = []
        self.order = []

    def push(self, item):
        if type(item) == int:
            if item not in self.stack:
                self.order.append(item)
                self.frequency.append(1)
            else:
                self.frequency[self.order.index(item)] = self.frequency[self.order.index(item)] + 1
            self.stack.append(item)
        else:
            print("Cannot push. FrequencyStack only takes integers.")

    def pop(self):
        if len(self.stack) == 0:
            print("Cannot pop. FrequencyStack is currently empty.")
        else:
            if self.frequency[self.order.index(self.stack[-1])] > 1:
                self.frequency[self.order.index(self.stack[-1])] = self.frequency[self.order.index(self.stack[-1])] - 1
            else:
                self.order.remove(self.stack[-1])
                self.frequency.remove(self.order.index([self.stack[-1]]))
            self.stack.pop()
    
    def print(self):
        print(self.stack)

        
fq = frequencyStack()
fq.push(7)
fq.push(3)
fq.push(2)
fq.push(1)
fq.pop()
fq.pop()
fq.print()