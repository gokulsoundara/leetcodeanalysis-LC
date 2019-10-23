class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        #count bits manually
        # def bitcounter(n):
        #     c = 0
        #     while n:
        #         c += n&1
        #         n>>=1
        #     return c
        # output = [0]
        # for i in range(1,num+1):
        #     a = output[i//2] + (i % 2)
        #     output.append(a)

        li = []
        for i in range(num+1):
            li.append(bin(i).count('1'))

        return li
