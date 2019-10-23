class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        last = len(s)-1
        for i in range(len(s)//2):
            s[i],s[last] = s[last], s[i]
            last-=1
        