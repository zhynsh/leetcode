# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0;
        flag2 = 0;
        l3 = ListNode();
        copy = l3;
        while flag == 1 or l1 != None or l2 != None:
            s = flag;
            flag = 0;
            if l1 != None:
                s = s + l1.val;
                l1 = l1.next;
            if l2 != None:
                s = s + l2.val;
                l2 = l2.next;
            if s >= 10:
                s = s - 10;
                flag = 1;
            if flag2 == 0:
                l3.val = s;
                flag2 = 1;
            else:
                temp = ListNode();
                temp.val = s;
                l3.next = temp;
                l3 = l3.next;
        return copy;