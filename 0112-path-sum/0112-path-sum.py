# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curnt_sum):
            if not node:
                return False
            curnt_sum += node.val
            if not node.right and not node.left:
                return curnt_sum == targetSum
            return (dfs(node.left, curnt_sum) or dfs(node.right, curnt_sum))
        return dfs(root, 0)
        
            
        