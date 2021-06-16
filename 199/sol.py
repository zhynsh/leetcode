#https://leetcode-cn.com/problems/binary-tree-right-side-view/
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        sol = []
        def rsv(rlist: List[TreeNode]):
            sol.append(rlist[-1].val)
            temp = []
            for node in rlist:
                if node.left != None:
                    temp.append(node.left)
                if node.right != None:
                    temp.append(node.right)
            if len(temp) > 0:
                rsv(temp)
        t = []
        t.append(root)
        rsv(t)
        return sol
