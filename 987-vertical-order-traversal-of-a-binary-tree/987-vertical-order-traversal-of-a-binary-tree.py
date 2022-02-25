# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = [(root, 0)]
        mapp = collections.defaultdict(list)
        
        while queue:
            nxt = []
            for node, vertical in queue:
                mapp[vertical].append(node.val)
                if node.left:
                    nxt.append((node.left, vertical - 1))
                if node.right:
                    nxt.append((node.right, vertical + 1))
                nxt.sort(key = lambda vertical: (vertical[1], vertical[0].val))
            queue = nxt
        for i in sorted(mapp):
            res.append(mapp[i])
        return res