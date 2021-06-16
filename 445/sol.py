#https://leetcode-cn.com/problems/add-two-numbers-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l1.val == 0:
            return l2
        if l2 == None or l2.val == 0:
            return l1
        def length(l: ListNode):
            if l == None:
                return 0
            return length(l.next) + 1
        len1 = length(l1)
        len2 = length(l2)
        if length(l1) > length(l2):
            long = l1
            longlen = len1
            short = l2
            shortlen = len2
        else:
            long = l2
            longlen = len2
            short = l1
            shortlen = len1
        longtemp = long
        shorttemp = short
        for i in range(longlen - shortlen):
            longtemp = longtemp.next
        #topflag = (longtemp.val + shorttemp.val >= 10)
        #sum = (longtemp.val + shorttemp.val) % 10
        sum = longtemp.val + shorttemp.val
        prev = ListNode(sum)
        sol = prev
        longtemp = longtemp.next
        shorttemp = shorttemp.next
        while longtemp and shorttemp:
            flag = False
            sum = (longtemp.val + shorttemp.val)
            prev = ListNode(sum, prev)
            longtemp = longtemp.next
            shorttemp = shorttemp.next
        #if longlen == shortlen:
            #if topflag:
                #return ListNode(1, sol)
            #return sol
        end = prev
        if longlen != shortlen:
            prev = ListNode(long.val)
            sol2 = prev
            long = long.next
            for i in range(longlen - shortlen - 1):
                prev = ListNode(long.val, prev)
                long = long.next
            sol.next = prev
        ptr = end
        while ptr.next:
            if ptr.val >= 10:
                ptr.val -= 10
                ptr.next.val += 1
            ptr = ptr.next
        if ptr.val >= 10:
            ptr.next = ListNode(1)
            ptr.val -= 10
        start = None
        while end:
            start = ListNode(end.val, start)
            end = end.next
        return start
