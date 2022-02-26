# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        mapp = collections.defaultdict(list)
        
        def dfs(node, level, column):
            if node:
                mapp[level].append(column)
                dfs(node.left, level+1, column*2)
                dfs(node.right, level+1, column*2+1)
        
        dfs(root, 0, 0)
        for level in mapp:
            #last-first+1
            ans = [max(mapp[level]) - min(mapp[level]) +1 for level in mapp]
        return max(ans)