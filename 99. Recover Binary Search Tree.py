# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    low = None
    high = None
    prev = None
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.subroutine(root)
        self.low.val , self.high.val = self.high.val, self.low.val
    def subroutine(self, root):
        if(root is None): return 
        self.subroutine(root.left)
        if(self.prev and self.prev.val > root.val and not self.low):
            self.low = self.prev
        if(self.prev and self.prev.val > root.val and self.low):
            self.high = root
        #print(root)
        self.prev = root
        self.subroutine(root.right)
        
