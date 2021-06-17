#https://leetcode-cn.com/problems/valid-number/
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s or s == "":
            return False
        def isint(s: str):
            if not s or s == '':
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            return s.isdigit()
        def isdot(s: str):
            if not s or s == '':
                return False
            if s[0] == '+' or s[0] == '-':
                s = s[1:]
            s2 = s.split('.')
            if len(s2) != 2:
                return False
            if (s2[0] == '') and (s2[1] == ''):
                return False
            if (s2[0].isdigit() or s2[0] == '') and (s2[1].isdigit() or s2[1] == ''):
                return True
            return False
        s = s.upper().split('E')
        if len(s) == 1:
            if isint(s[0]) or isdot(s[0]):
                return True
        if len(s) == 2 and isint(s[1]):
            if isint(s[0]) or isdot(s[0]):
                return True
        return False
