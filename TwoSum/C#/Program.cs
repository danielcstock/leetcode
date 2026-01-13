using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var seen = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++){
            var complement = target - nums[i];

            if (seen.TryGetValue(complement, out int index)) 
                return new[] {index, i};
            seen[nums[i]] = i;
        }
        return null;
    }
}