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

            #iterative step
            
            #recursivley call left and right
            left = dfs(curr.left)
            right = dfs(curr.right)

            #if the abs value difference is greater than 1 then change var
            if abs(left - right) > 1:
                self.isValid = False


            return max(left, right) + 1

        

        dfs(root)
        return self.isValid
        