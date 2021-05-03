#https://leetcode-cn.com/problems/clone-graph/
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None;
        def helper(node: 'Node', existed: List[int]) -> 'Node':
            copy = Node();
            copy.val = node.val;
            existed.append(copy.val);
            existedNode.append(copy);
            for i in range(0, len(node.neighbors)):
                if node.neighbors[i].val not in existed:
                    temp = helper(node.neighbors[i], existed);
                    #temp.neighbors.append(copy);
                    copy.neighbors.append(temp);
                else:
                    flag = 0;
                    for j in range(0, len(copy.neighbors)):
                        if copy.neighbors[j].val == node.neighbors[i].val:
                            flag = 1;
                    if flag == 0:
                        for j in range(0, len(existedNode)):
                            if existedNode[j].val == node.neighbors[i].val:
                                copy.neighbors.append(existedNode[j]);
            return copy;
        existed = [];
        existedNode = [];
        return helper(node, existed);