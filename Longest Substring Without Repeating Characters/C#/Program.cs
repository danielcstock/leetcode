public class Solution
{
    public int LengthOfLongestSubstring(string s)
    {
        var counts = new Dictionary<char, int>();
        int start = 0;
        int maxWindowLength = 0;

        for (int i = 0; i < s.Length; i++)
        {
            char letter = s[i];
            if (!counts.ContainsKey(letter)) counts[letter] = 0;
            counts[letter]++;

            while (counts[letter] > 1)
            {
                char deletingLetter = s[start];
                counts[deletingLetter]--;
                if (counts[deletingLetter] == 0) counts.Remove(deletingLetter);
                start++;
            }
            maxWindowLength = Math.Max(maxWindowLength, i - start + 1);
        }
        return maxWindowLength;
    }
}