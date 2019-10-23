# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(l,r):
            if l>=r:
                return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            node.left = helper(l, mid)
            node.right = helper(mid+1,r)
            return node
        
        return helper(0, len(nums))