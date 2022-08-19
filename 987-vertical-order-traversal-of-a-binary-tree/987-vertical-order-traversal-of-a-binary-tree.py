# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        m = dict()
        #create a map of horizontal distance m[hd] = {level:[root.val]}
        def get_vertical_order(root, hd, level):
            if not root:
                return
            if m.get(hd):
                if m[hd].get(level):
                    m[hd][level].append(root.val)
                else:
                    m[hd][level] = [root.val]
            else:
                m[hd] = {level:[root.val]}
            get_vertical_order(root.left, hd - 1, level+1)
            get_vertical_order(root.right, hd + 1, level+1)
        get_vertical_order(root, 0, 1)
        ans = []
        for keys in sorted(m.keys()):
            temp = []
            for levels in sorted(m[keys]):
                temp+=sorted(m[keys][levels])
            ans.append(temp)
        return ans
                