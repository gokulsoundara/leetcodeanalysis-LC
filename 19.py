# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dhead = ListNode(0)
        dhead.next = head
        fast,slow,leng = head,head,head

        length = 0
        #calculate lenght of ll
        while leng:
            leng = leng.next
            length+=1
        #where remove element larger than lenght of ll
        if length<n:
            return
        #where remove the head node
        if length==n:
            return head.next

        #fast cycle to skip n node
        for i in range(n):
            fast = fast.next
        prev = head
        while fast:
            prev = slow
            fast,slow = fast.next,slow.next

        #delete nth node from back
        prev.next = slow.next
        return dhead.next
