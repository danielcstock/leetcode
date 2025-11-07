class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        result = ''
        wordSize = len(s)
        index = 0
        newString = ''
        groupSize = numRows * 2 - 2

        for i in range(int(wordSize/groupSize)+1):
            if index < len(s):
                result += s[index]
                newString += s[index+1:groupSize*(i+1)]
            index += groupSize
        
        print(newString)
        result += self.convert(newString, numRows-1)
        return result
    
sol = Solution()
print(sol.convert('PAYPALISHIRING', 3))
# PAHNAPLSIIGYIR