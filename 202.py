class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:return True
        # if n>1 and n<10: return False

        def squaresum(num):
            val = 0
            while num:
                rem = num%10
                val += rem**2
                num =num//10
            return val

        setv = set()
        setv.add(n)
        while True:
            n = squaresum(n)
            if n in setv:
                return False
            if n ==1:
                return True
            setv.add(n)
            
