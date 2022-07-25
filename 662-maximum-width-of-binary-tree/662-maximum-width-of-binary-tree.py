# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        if not root:
            return 0
        ans = 0
        q = collections.deque()
        q.append([root, 0])
        while q:
            size = len(q)
            mmin = q[0][1]
            first, last = 0, 0
            for i in range(size):
                currID = q[0][1] - mmin
                node = q[0][0]
                
                q.popleft()
                
                if i == 0:
                    first = currID
                if i == size - 1:
                    last = currID
                if node.left:
                    q.append([node.left, currID*2 + 1])
                if node.right:
                    q.append([node.right, currID*2 + 2])
                
            ans = max(ans, last-first+1)
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """mapp = collections.defaultdict(list)
        
        def dfs(node, level, column):
            if node:
                mapp[level].append(column)
                dfs(node.left, level+1, column*2)
                dfs(node.right, level+1, column*2+1)
        
        dfs(root, 0, 0)
        for level in mapp:
            #last-first+1
            ans = [max(mapp[level]) - min(mapp[level]) +1]
        return max(ans)"""
        