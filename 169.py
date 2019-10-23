class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)//2
        tab = {}
        for i in nums:
            tab[i] = tab.get(i,0)+1
            if tab[i]>n:
                return i