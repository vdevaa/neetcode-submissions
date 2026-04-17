# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        result = []


        def dfs(currNode, height):
            if not currNode:
                return None

            if len(result) == height:
                result.append(currNode.val)
            
            #recurivly call on right first
            dfs(currNode.right, height + 1)
            dfs(currNode.left, height + 1)

        dfs(root,0)
        return result

