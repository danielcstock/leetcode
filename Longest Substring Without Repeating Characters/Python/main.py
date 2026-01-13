class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substring = {}
        maxWindowLength = 0
        start = 0

        for end in range(len(s)):
            letter = s[end]
            substring[letter] = substring.get(letter, 0) + 1

            while substring[letter] > 1:
                letLetter = s[start]
                substring[letLetter] -= 1
                if substring[letLetter] == 0:
                    del substring[letLetter]
                start += 1

            maxWindowLength = max(maxWindowLength, end - start + 1)

        return maxWindowLength