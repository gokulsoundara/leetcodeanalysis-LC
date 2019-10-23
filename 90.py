class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        def backtrack(start):
            res.append(temp[:])
            for i in range(start, len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop(-1)


        res = []
        temp = []
        backtrack(0)
        return res
