#https://leetcode-cn.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False;
        if x == 0:
            return True;
        y = str(x);
        for i in range(0, int(len(y) / 2)):
            if y[i] != y[- i - 1]:
                return False;
        return True;