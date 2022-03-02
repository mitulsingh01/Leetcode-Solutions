# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0
        def helper(bound):
            if self.i >= len(preorder) or preorder[self.i] >= bound:
                return None
            val = preorder[self.i]
            self.i += 1
            root = TreeNode(val)
            root.left = helper(val)
            root.right = helper(bound)
            
            return root
        
        return helper(float("inf"))