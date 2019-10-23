class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target:
            return []

        def backtrack(start):
            if sum(temp)==target:
                res.append(temp[:])
            for i in range(start,len(candidates)):
                if sum(temp)<target:
                    temp.append(candidates[i])
                    backtrack(i)
                    temp.pop()

        res = []
        temp = []
        backtrack(0)
        return res



#         candidates.sort()

#         l,r = 0,len(candidates)-1
#         li = []
#         while l<r:
#             if r >=target:
#                 li.append([r])
#                 r-=1
#             else:
#                 if l+r>target:
#                     r -=1
#                 elif l+r==target:
#                     li.append([l,r])
#                     r-=1
#                 else:
#                     if l%target==0:
#                         li.append([l]*l//target)
