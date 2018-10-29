# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lp = l1.val + l2.val
        if lp > 9:
           ad = 1
           out = ListNode(lp-10)
        else:
           ad = 0
           out = ListNode(lp)

        loop = out

        while True:
            if l1.next == None and l2.next == None and ad == 0:
                break
            if l1.next != None:
               l1 = l1.next
            else:
               l1 = ListNode(0)
            if l2.next != None:
               l2 = l2.next
            else:
               l2 = ListNode(0)

            lp = l1.val + l2.val + ad
            if lp > 9:
               ad = 1
               loop.next = ListNode(lp-10)

            else:
               ad = 0
               loop.next = ListNode(lp)

            loop = loop.next
            return out
