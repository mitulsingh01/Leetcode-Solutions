# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        level = 0
        self.helper(root, 0, ans)
        return ans
    
    def helper(self, root, level, ans):
        if root == None:
            return
        if level == len(ans):
            ans.append(root.val)
        self.helper(root.right, level+1, ans)
        self.helper(root.left, level+1, ans)