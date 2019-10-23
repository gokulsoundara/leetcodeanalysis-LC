class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            ans = ""
            if i%3==0:
                ans += "Fizz"
            if i%5 == 0:
                ans += "Buzz"
            if not ans:
                ans = str(i)
            res.append(ans)
            
        return res