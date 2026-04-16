# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def dfs(rootNode, height):

            if not rootNode: # base case
                return None
            
            if len(result) == height:
                result.append([])
            
            result[height].append(rootNode.val) # add value to list (index is level)

            # recursivly call
            dfs(rootNode.left, height + 1)
            dfs(rootNode.right, height + 1)
        
        dfs(root,0)

        return result

            

        