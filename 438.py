class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        if len(p)>len(s):
            return []

        table = {}
        window={}
        for char in p:
            table[char]  = table.get(char,0)+1
            window[char] = 0

        start,end = 0,0
        li = []
        counter = len(p)

        while end<len(s):
            while end-start<len(p):
                cur = s[end]
                if cur in window:
                    window[cur]+=1
                end+=1
            if window==table:
                li.append(start)
            if s[start] in window:
                window[s[start]]-=1
            start+=1
        return li
