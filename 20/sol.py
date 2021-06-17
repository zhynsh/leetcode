#https://leetcode-cn.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for i in s:
            if i == '(' or i == "[" or i == "{":
                temp.append(i)
            else:
                if temp == []:
                    return False
                t = temp.pop()
                if t == "(" and i == ")":
                    continue
                if t == "[" and i == "]":
                    continue
                if t == "{" and i == "}":
                    continue
                return False
        if temp == []:
            return True
        return False
