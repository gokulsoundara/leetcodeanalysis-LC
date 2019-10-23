# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if (not p and q) or (not q and p):
            return False

        def preorder(p,q):
            if not p  and q or not q and p:
                return False
            if not p and not q:
                return True
            if p.val != q.val:
                return False
            return preorder(p.left,q.left) and preorder(p.right,q.right)

        return preorder(p,q)
