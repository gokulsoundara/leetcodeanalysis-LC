class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        l = range(1,n+1)

        def backtrack(start):
            if len(temp)==k:
                res.append(temp[:])
            for i in range(start,len(l)):
                temp.append(l[i])
                backtrack(i+1)
                temp.pop()

        res,temp = [],[]
        backtrack(0)
        return res
