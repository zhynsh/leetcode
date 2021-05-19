#https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hashidx = dict();
        for i in range(len(inorder)):
            hashidx[inorder[i]] = i;
        def lr(a: int, b: int):
            if hashidx[a] < hashidx[b]:
                return True;
            else:
                return False;
        root = TreeNode();
        root.val = preorder[0];
        for i in range(1, len(preorder)):
            ptr = root;
            while 1:
                if lr(preorder[i], ptr.val):
                    if ptr.left != None:
                        ptr = ptr.left;
                    else:
                        temp = TreeNode();
                        temp.val = preorder[i];
                        ptr.left = temp;
                        break;
                else:
                    if ptr.right != None:
                        ptr = ptr.right;
                    else:
                        temp = TreeNode();
                        temp.val = preorder[i];
                        ptr.right = temp;
                        break;
        return root;
