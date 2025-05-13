# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        mergedList = []
        
        for node in list1:
            if not mergedList:
                mergedList.append(node.val)
            else:
                for i in range(len(mergedList)):
                    if mergedList[i] > node.val:
                        mergedList.insert(node.val, i])
                        break
        
        for node in list2:
            if not mergedList:
                mergedList.append(node.val)
            else:
                for i in range(len(mergedList)):
                    if mergedList[i] > node.val:
                        mergedList.insert(node.val, i])
                        break
        
        return mergedList
                
s = Solution()
ln = ListNode()