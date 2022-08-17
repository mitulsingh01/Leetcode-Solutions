# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
        
        """inorder = []
        curr = root
        while curr:
            if curr.left == None:
                inorder.append(curr.val)
                curr =  curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right == None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        return inorder"""
        
        
        """ans = []
        self.helper(root, ans)
        return ans
    
    def helper(self, root, ans):
        if root:
            self.helper(root.left, ans)
            ans.append(root.val)
            self.helper(root.right, ans)"""
            
    """
    Iterative Solution
    
    """