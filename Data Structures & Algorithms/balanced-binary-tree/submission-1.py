# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.isValid = True

        def dfs(curr):
            #base case
            if not curr:
                return 0

            #iterativee step

            #recurvly call left and right
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left - right) > 1:#check if left and right difference is more than 1
                self.isValid = False
                #if it is then set to false
            
            return max(left,right) + 1

        dfs(root)
        return self.isValid

        