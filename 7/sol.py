#https://leetcode-cn.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        if x == -pow(2, 31):
            return 0;
        i = 0;
        flag = 0;
        sol = 0;
        if x < 0:
            flag = 1;
            x = -x;
        while x > 0:
            if i == 9 and sol > 214748364:
                return 0;
            temp = x % 10;
            x = int((x - temp) / 10);
            i = i + 1;
            sol = sol * 10 + temp;
        if flag == 1:
            sol = -sol;
        return sol;
