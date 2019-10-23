class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return []

        def ispalindrom(s):
            return list(s)==list(s)[::-1]

        def backtrack(start):
            if start==len(s):
                res.append(temp[:])
            for i in range(start,len(s)):
                sub = s[start:i+1]
                if not ispalindrom(sub):
                    continue
                temp.append(sub)
                backtrack(i+1)
                temp.pop()

        res = []
        temp = []
        backtrack(0)
        return res

        
