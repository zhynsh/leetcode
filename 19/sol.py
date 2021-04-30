# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        copy = head;
        while head != None:
            temp = head;
            for i in range(0, n):
                temp = temp.next;
            if temp == None:
                return copy.next;
            if temp.next == None:
                head.next = head.next.next;
                return copy;
            head = head.next;