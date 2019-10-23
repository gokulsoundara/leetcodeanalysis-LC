class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        minlen = 0
        for each in strs:
            if len(each)>minlen:
                minlen = len(each)
                minword = each

        minst = ""
        if not minlen:
            return ""

        li = []
        for word in strs:
            st = ""
            for idx,char in enumerate(word):
                if char==minword[idx]:
                    st+=char
                else:
                    break
            li.append(st)

        minw = ""
        for each in li:
            if len(each)<=minlen:
                minw = each
                minlen=len(each)
        return minw
