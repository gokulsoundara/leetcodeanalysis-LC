class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tab = {}
        for i in s:
            tab[i] = tab.get(i,0)+1
            
        for i in t:
            if i not in tab:
                return False 
            tab[i] = tab.get(i)-1
            if tab[i]<0:
                return False 
            
        for k,v in tab.items():
            if v:
                return False
            
        return True 