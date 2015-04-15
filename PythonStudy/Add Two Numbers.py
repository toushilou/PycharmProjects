#! /usr/bin/env python
#coding=utf-8
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        moreThanTen = False
        head = ListNode(0)
        node = head
        while True:
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                l1 = ListNode(0)
            elif l2 == None:
                l2 = ListNode(0)
            if moreThanTen:
                x = l1.val + l2.val + 1
                moreThanTen = False
            else:
                x = l1.val + l2.val
            if x >= 10:
                x -= 10
                moreThanTen = True
            l1 = l1.next
            l2 = l2.next
            node = ListNode(x)
            node.next = ListNode(0)
        return head
        

if __name__ == '__main__':
    s = Solution()
    head = l1 = ListNode(2)
    l3 = [5,6,4]            
