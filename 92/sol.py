#https://leetcode-cn.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head;
        copy = None;
        if left > 1:
            copy = head;
        for i in range(0, left - 2):
            head = head.next;
        if left == 1:
            n1 = None;
            n2 = head;
        else:
            n1 = head;
            n2 = head.next;
        head = head.next;
        prev = n2;
        if left > 1:
            head = head.next;
        nex = None;
        for i in range(0, right - left):
            nex = head.next;
            head.next = prev;
            prev = head;
            head = nex;
        if n1 != None:
            n1.next = prev;
        else:
            copy = prev;
        if nex != None:
            n2.next = nex;
        else:
            n2.next = None;
        return copy;