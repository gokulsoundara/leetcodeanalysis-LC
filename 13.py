class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        tab = {"I" :   1,"V" : 5,"X"  :10,"L"   :50,"C" : 100,"D":500,"M":1000}
        
        res = 0 
        prev = float('-inf')
        for i in reversed(s):
            val = tab.get(i)
            if val < prev:
                res -= prev
                val = prev - val 
            res += val
            prev = val 
                
        return res