class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        windowlen = len(needle)

        if not needle:
            return 0
        if windowlen>len(haystack):
            return -1

        for i in range(len(haystack)-windowlen+1):
            if haystack[i:i+windowlen] == needle:
                return i

        return -1 
