#https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root: 'TreeNode', a: 'TreeNode'):
            if root is a:
                return True
            if root.left != None and search(root.left, a):
                return True
            if root.right != None and search(root.right, a):
                return True
            return False
        sol = root
        if root.left != None and search(root.left, p) and search(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.right != None and search(root.right, p) and search(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        return root
