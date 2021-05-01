#https://leetcode-cn.com/problems/rotate-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        depth = 0;
        copy = head;
        end = head;
        while head != None:
            if head.next == None:
                end = head;
            head = head.next;
            depth = depth + 1;
        if depth == 0:
            return None;
        k = k % depth;
        if k == 0:
            return copy;
        count = 0;
        head = copy;
        while count < depth - k - 1:
            head = head.next;
            count = count + 1;
        begin = head.next;
        head.next = None;
        end.next = copy;
        return begin;