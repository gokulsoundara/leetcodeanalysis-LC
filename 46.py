class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start):
            if len(temp)==len(nums):
                res.append(temp[:])
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop(-1)


        res = []
        temp = []
        backtrack(0)
        return res
