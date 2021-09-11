class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return "1"
        
        lastStr = self.countAndSay(n - 1)
        
        
        num = 0
        digit = None
        res = ""
        for i in range(len(lastStr)):
            if digit!=None and digit != lastStr[i]:
                res += str(num)
                res += digit
                digit = lastStr[i]
                num = 1
            else:
                digit = lastStr[i]
                num += 1
                
        res += str(num)
        res += digit
        
        return res