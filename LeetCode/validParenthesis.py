class Solution(object):
    def isValid(self, s):
        validClosed = [")", "]", "}"]        
        valid = ["(", ")", "[", "]", "{", "}"] 
        openStack = []
        for i in range(len(s)):
            if s[i] in validClosed:
                if not openStack:
                    return False
                else:
                    if openStack[-1] == valid[valid.index(s[i]) - 1]:
                        openStack.pop()
                    else:
                        return False
            else:
                openStack.append(s[i])
        if not openStack:
            return True
        else:
            return False