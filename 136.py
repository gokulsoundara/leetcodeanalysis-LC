class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         table = {}
#         for i in nums:
#             table[i] = table.get(i,0)+1
            
#         for i,k in table.items():
#             if k==1:
#                 return i
            
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
        
        return ans