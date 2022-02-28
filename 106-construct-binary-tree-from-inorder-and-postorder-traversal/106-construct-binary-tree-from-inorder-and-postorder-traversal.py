# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        mapp = {}
        for i in range(len(inorder)):
            mapp[inorder[i]] = i
        
        def buildHelper(inorder, iStart, ie, postorder, ps, pe, mapp):
            if ps > pe or iStart > ie:
                return None
            
            root = TreeNode(postorder[pe])
            inRoot = mapp[postorder[pe]]
            numsLeft = inRoot - iStart
            
            root.left = buildHelper(inorder, iStart, inRoot - 1, postorder, ps, ps + numsLeft - 1, mapp)
            root.right = buildHelper(inorder, inRoot + 1, ie, postorder, ps + numsLeft, pe - 1, mapp)
            
            return root
        
        return buildHelper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1, mapp) 
    
    