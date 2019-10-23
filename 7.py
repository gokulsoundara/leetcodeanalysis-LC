class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MIN = -2**31
        INT_MAX = 2**31 -1

        if x >= 2147483647 or x<=-2147483648:
            return 0

        minus = False
        if x<0:
            minus = True

        num = 0
        x = abs(x)
        while x:
            num=num*10 + x%10
            x = x//10

        if minus:
            num = - num
        if (num >= 2147483647) or (num<=-2147483648):
            return 0
        return num
