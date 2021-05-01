#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head;
        copy = head;
        if head.val == head.next.val:
            while 1:
                if head.next.next == None:
                    if head.val == head.next.val:
                        return None;
                    else:
                        return head.next;
                if head.val != head.next.val and head.next.val != head.next.next.val:
                    copy = head.next;
                    break;
                head = head.next;
        head = copy;
        while 1:
            if head.next == None or head.next.next == None:
                return copy;
            if head.next.val != head.next.next.val:
                head = head.next;
            else:
                temp = head.next;
                while 1:
                    if temp.next == None or temp.next.val != temp.val:
                        head.next = temp.next;
                        break;
                    temp = temp.next;