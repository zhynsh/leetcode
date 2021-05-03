#https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return [];
        def helper(root: TreeNode, sol: List[int]):
            if root.left != None:
                helper(root.left, sol);
            sol.append(root.val);
            if root.right != None:
                helper(root.right, sol);
        sol = [];
        helper(root, sol);
        return sol;