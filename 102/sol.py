#https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return [];
        prevlev = [];
        nextlev = [];
        sol = [];
        soltemp = [];
        prevlev.append(root);
        while len(prevlev) > 0:
            while len(prevlev) > 0:
                temp = prevlev.pop(0);
                if temp.left != None:
                    nextlev.append(temp.left);
                if temp.right != None:
                    nextlev.append(temp.right);
                soltemp.append(temp.val);
            sol.append(soltemp);
            prevlev = nextlev;
            nextlev = [];
            soltemp = [];
        return sol;
