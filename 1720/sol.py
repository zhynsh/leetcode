#https://leetcode-cn.com/problems/decode-xored-array/
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        sol = [];
        sol.append(first);
        for i in range(0, len(encoded)):
            sol.append(encoded[i] ^ sol[-1]);
        return sol;