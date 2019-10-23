class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # ans = [[]]
        # for n in nums:
        #     ans = [prev + curr for prev in ans for curr in [[], [n]]]
        # return ans

        def backtrack(start):
            res.append(temp[:])
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(i+1)
                temp.pop(-1)


        res = []
        temp = []
        backtrack(0)
        return res
