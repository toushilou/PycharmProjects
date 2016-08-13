class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        while listNode.next != None:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]


s = Solution()
listNode = ListNode()
s.printListFromTailToHead()