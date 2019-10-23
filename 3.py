class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        start,end = 0,0
        maxlen = 0
        setv = set()
        leng = 0

        while end<len(s):
            if s[end] not in setv:
                setv.add(s[end])
                leng +=1
                end +=1
            else:
                while end>start:
                    if s[start] in setv:
                        setv.remove(s[start])
                        start+=1
                        leng-=1
                        break
                    start+=1
                    leng -=1
            maxlen = max(maxlen, leng)

        return maxlen
