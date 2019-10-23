class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tab = set()
        
        for i in nums:
            if i in tab:
                return True
            tab.add(i)
            
        return False 