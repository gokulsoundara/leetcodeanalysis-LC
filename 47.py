class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        def backtrack(start):
            if len(temp)==len(nums):
                res.append(temp[:])
            for i in range(len(nums)):
                if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):
                    continue
                used[i]=True
                temp.append(nums[i])
                backtrack(i+1)
                used[i]=False
                temp.pop(-1)


        res = []
        temp = []
        used = [False]*len(nums)
        backtrack(0)
        return res
