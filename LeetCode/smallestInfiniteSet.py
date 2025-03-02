class SmallestInfiniteSet(object):

    def __init__(self):
        self.removedSet = []

    def popSmallest(self): # Adds to the removedSet
        if not self.removedSet:
            self.removedSet.append(1)
            return 1
        else:
            for i in range(1, len(self.removedSet) + 1):
                if i not in self.removedSet:
                    return self.removedSet.append(i)
            return self.removedSet.append(self.removedSet[-1] + 1)

    def addBack(self, num): # Removes from the removedSet
        if num in self.removedSet:
            self.removedSet.remove(num)

obj = SmallestInfiniteSet()
pm = obj.popSmallest() # null
pm = obj.popSmallest() # null
pm = obj.popSmallest() # null
obj.addBack(1)
pm = obj.popSmallest()
pm = obj.popSmallest()
obj.addBack(2)
pm = obj.popSmallest()
print(obj.removedSet)

# Instead of creating a set with all numbers, create a set with the numbers you remove
# Edge cases: 