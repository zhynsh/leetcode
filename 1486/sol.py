#https://leetcode-cn.com/problems/xor-operation-in-an-array/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        sol = start;
        for i in range(1, n):
            sol = sol ^ (start + 2 * i);
        return sol;