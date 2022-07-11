# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Reverse Preorder Traversal
        def helper(node, level, ds):
            if node == None:
                return
            if level == len(ds):
                ds.append(node.val)
            helper(node.right, level+1, ds)
            helper(node.left, level+1, ds)
        ds = []
        helper(root, 0, ds)
        return ds
                