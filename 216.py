class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = range(1,10)

        def backtrack(start):
            if sum(temp)==n and len(temp)==k:
                res.append(temp[:])
            for i in range(start,len(nums)):
                if sum(temp)<n:
                    temp.append(nums[i])
                    backtrack(i+1)
                    temp.pop()

        temp,res = [],[]
        backtrack(0)
        return res
