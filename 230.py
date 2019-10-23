# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # c = 0
    # result = 0
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return
        li = []
        def inorder(root):
            if not root:
                return
            if len(li)<=k:
                inorder(root.left)
                li.append(root.val)
                inorder(root.right)

        inorder(root)
        return li[k-1]
