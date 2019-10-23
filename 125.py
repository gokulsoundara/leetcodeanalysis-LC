class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        def modifer(s):
            st = ""
            for char in s.lower():
                if char.isalnum():
                    st+=char
            return st

        st = modifer(s)
        l,r = 0,len(st)-1
        while l<r:
            if st[l]==st[r]:
                l+=1
                r-=1
            else:
                return False
        return True


                
