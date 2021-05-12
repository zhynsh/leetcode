#https://leetcode-cn.com/problems/xor-queries-of-a-subarray/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        sol = [];
        for i in range(0, len(queries)):
            temp = arr[queries[i][0]];
            index = queries[i][0];
            for j in range(0, queries[i][1] - queries[i][0]):
                index = index + 1;
                temp = temp ^ arr[index];
            sol.append(temp);
        return sol;