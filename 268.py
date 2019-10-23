class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):
            nums[nums[i]%n]+=n
            
        for i in range(1,len(nums)):
            if nums[i]//n==0:
                return i
        return 0
            
#         tot = sum(nums)
#         n = len(nums)
#         val = (n * (n+1))/2
#         return abs(tot-val)
    