class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            text = str(x)[::-1]
        else:
            text = str(x)[0] + '' + str(x)[:0:-1]
        reversed = int(text)
        reversed_int = int(reversed)
        if -2**31 <= reversed_int <= 2**31 - 1:
            return reversed_int
        return 0