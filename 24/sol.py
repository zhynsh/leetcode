#https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = head;
        copy = head;
        if temp != None and temp.next != None:
            copy = copy.next; 
        while temp != None and temp.next != None:
            head = temp;
            temp = temp.next.next;
            head.next.next = head;
            if temp != None and temp.next != None:
                head.next = temp.next;
            else:
                head.next = temp;
        return copy;