#https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return [];
        prevlev = [];
        nextlev = [];
        sol = [];
        soltemp = [];
        flag = 1;
        prevlev.append(root);
        while len(prevlev) > 0:
            while len(prevlev) > 0:
                temp = prevlev.pop(0);
                if temp.left != None:
                    nextlev.append(temp.left);
                if temp.right != None:
                    nextlev.append(temp.right);
                if flag == 1:
                    soltemp.append(temp.val);
                else:
                    soltemp.insert(0, temp.val);
            sol.append(soltemp);
            prevlev = nextlev;
            nextlev = [];
            soltemp = [];
            flag = -flag;
        return sol;