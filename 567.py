class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if not s1 or not s2:
            return False

        if len(s1)>len(s2):
            return False

        table = {}

        for char in s1:
            table[char]=table.get(char,0)+1

        start,end = 0,0
        counter = len(table)
        li = []

        while end<len(s2):
            cur = s2[end]
            if cur in table:
                table[cur]-=1
                if table[cur]==0: counter -=1

            end+=1
            while counter == 0:
                first = s2[start]
                if (first in table):
                    if (end-start ==len(s1)):
                        return True
                    else:
                        table[first]+=1
                        if table[first]>0:counter+=1
                start +=1

        return False

                    
