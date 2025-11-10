class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1 and not s.isdigit():
            return 0
        elif s.isdigit():
            x = int(s)
        else:
            text = self.trimStart(s)
            sign = -1
            if len(text) > 1 and not text[0].isdigit():
                sign = text[0] == '-'
                text = text[1:]
            elif not text[0].isdigit:
                return 0
            if not text[0].isdigit():
                return 0
            if len(text) > 1:
                text = self.trimEnd(text)
            
            x = self.convertToInt(text)
            if sign:
                x *= -1
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x < INT_MIN:
            return INT_MIN
        if x > INT_MAX:
            return INT_MAX
        return x
    
    """
    :type s: str
    :rtype: str
    """
    def trimStart(self, s):
        if len(s) > 1:
            if s[0].isspace():
                return self.trimStart(s[1:])
            elif not s[0].isdigit() and s[0] != '-' and s[0] != '+':
                return '0'
        return s
    
    """
    :type s: str
    :rtype: str
    """
    def trimEnd(self, s):
        if s.isdigit():
            return s
        return self.trimEnd(s[:-1])

    """
    :type s: str
    :rtype: int
    """
    def convertToInt(self, s):
        if s.isdigit():
            return int(s)
        elif not s[0].isdigit():
            return 0
        
        if len(s) == 1 and s.isdigit():
            return int(s)
        return self.convertToInt(s[0])*10**(len(s)-1) + self.convertToInt(s[1:])
    
s = Solution()
print(s.myAtoi('1337c0d3'))