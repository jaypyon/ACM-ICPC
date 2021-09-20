# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## I think we can use a datastructure which name is stack
        stack = list()
        result = list()
        now = root
        while now is not None or len(stack)>0:
            while now is not None:
                stack.append(now)
                result.append(now.val)
                now = now.left
            now = stack.pop()
            
            now = now.right

        return result
