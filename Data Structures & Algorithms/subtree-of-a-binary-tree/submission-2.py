# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None and subRoot is None:
            return True
        if root is None:
            return False
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        if self.isSameTree(root,subRoot):
            return True
        
        return left or right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False
        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right,q.right)

        # return (left and right)
        if left != right or left is False and right is False:
            return False

        return True