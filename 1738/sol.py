#https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value/
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        sol = [];
        orders = [];
        for i in range(len(matrix)):
            sol.append([]);
            for j in range(len(matrix[0])):
                temp = matrix[i][j];
                if i > 0:
                    temp = temp ^ sol[i - 1][j];
                if j > 0:
                    temp = temp ^ sol[i][j - 1];
                if i > 0 and j > 0:
                    temp = temp ^ sol[i - 1][j - 1];
                sol[i].append(temp);
                orders.append(temp);
        orders.sort();
        return orders[-k];
