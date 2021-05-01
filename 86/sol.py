#https://leetcode-cn.com/problems/partition-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        copy = head;
        lbegin = None;
        rbegin = None;
        while head != None and (lbegin == None or rbegin == None):
            if head.val < x:
                if lbegin == None:
                    lbegin = head;
            else:
                if rbegin == None:
                    rbegin = head;
            head = head.next;
        if lbegin == None or rbegin == None:
            return copy;
        head = copy;
        copy = lbegin;
        temp = rbegin;
        while head != None:
            if head.val < x:
                if head != lbegin:
                    lbegin.next = head;
                    lbegin = lbegin.next;
            else:
                if head != rbegin:
                    rbegin.next = head;
                    rbegin = rbegin.next;
            head = head.next;
        lbegin.next = temp;
        rbegin.next = None;
        return copy;