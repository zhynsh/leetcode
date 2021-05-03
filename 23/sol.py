#https://leetcode-cn.com/problems/merge-k-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        copy = None;
        ptr = copy;
        p = 0;
        while p < len(lists):
            if lists[p] == None:
                del lists[p];
            else:
                p = p + 1;
        while len(lists) > 0:
            for k in range(0, len(lists)):
                if lists[k] != None:
                    min = lists[k].val;
            for i in range(0, len(lists)):
                if lists[i] != None and lists[i].val < min:
                    min = lists[i].val;
            for j in range(0, len(lists)):
                if j >= len(lists):
                    break;
                if lists[j] != None and lists[j].val == min:
                    if copy == None:
                        copy = lists[j];
                        ptr = copy;
                    else:
                        ptr.next = lists[j];
                        ptr = ptr.next;
                    lists[j] = lists[j].next;
                    if lists[j] == None:
                        del lists[j];
                        j = j - 1;
        return copy;
