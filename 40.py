class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target:
            return []
        candidates.sort()

        def backtrack(start):
            if sum(temp)==target:
                res.append(temp[:])
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]: continue
                if sum(temp)<target:
                    temp.append(candidates[i])
                    backtrack(i+1)
                    temp.pop()

        res = []
        temp = []
        backtrack(0)
        return res
