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
            if not curr:
                return 0
            
            #iterative step

            #recurvely call left and right and set them
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.result = max(self.result, left + right) #set the max result to the current max if capable

            return max(left, right) + 1#return 1 + max of left and right

        dfs(root)
        return self.result
        