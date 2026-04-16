# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.result = 0

        def dfs(curr):

            #base case
            if not curr:
                return 0


            #iterative step

            left = dfs(curr.left)#recursily call left and right
            right = dfs(curr.right)
            self.result = max(left + right, self.result)
            #see if it gives us a new max

            return 1 + max(left,right)

        

        dfs(root)
        return self.result
        