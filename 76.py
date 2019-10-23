class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        table = {}
        for char in t:
            if char not in table:
                table[char]=1
            else:
                table[char]+=1

        start,end = 0,0
        length = len(s)
        counter = len(table)
        MAX_LEN = float("inf")
        st = ""

        while end<length:
            cur = s[end]
            if cur in table:
                table[cur]-=1
                if table[cur]==0:
                    counter-=1

            while counter==0:
                first = s[start]
                if first in table:
                    table[first]+=1
                    if table[first]>0:
                        if MAX_LEN>len(s[start:end+1]):
                            st = s[start:end+1]
                            MAX_LEN= len(st)
                        counter+=1
                start +=1
            end +=1

        return st
