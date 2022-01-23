# Data Assessment Prep Solutions


# Solution 2.2.1
data = ["abxxz,0001","aaxyz,0002","abcyz,0003"]

def returnLargest(data):
    id = "start"
    base = 0
    for obj in data:
        if int(obj[6:]) > base:
            base = int(obj[6:])
            id = obj[:5]
    return id

print(data)
print(returnLargest(data))
    
