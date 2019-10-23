# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        def totalsum(root):
            if not root:
                return 0
            if root.val >=L and root.val<=R:
                return root.val+totalsum(root.left) + totalsum(root.right)
            if root.val<L:
                return totalsum(root.right)
            if root.val>R:
                return totalsum(root.left)

        return totalsum(root)
