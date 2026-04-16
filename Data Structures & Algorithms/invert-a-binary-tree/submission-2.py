# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #base case
        if not root:
            return None

        #iterative step

        self.invertTree(root.left)#recursively call of left and right children
        self.invertTree(root.right)

        temp = root.left #swap children of root
        root.left = root.right
        root.right = temp

        

        return root 
        