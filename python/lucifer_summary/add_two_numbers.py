'''
2. Add Two Numbers
Medium

6995

1805

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 != None or l2 != None or carry != 0:
            val1 = 0 if l1 == None else l1.val
            val2 = 0 if l2 == None else l2.val
            n = ListNode((val1 + val2 + carry) % 10)
            carry = 1 if val1 + val2 + carry >= 10 else 0
            cur.next = n
            cur = cur.next
            l1 = None if l1 == None else l1.next
            l2 = None if l2 == None else l2.next
        return dummy.next
