using System;
using System.Collections.Generic;

public class Solution {
    public int TotalFruit(int[] fruits) {
        var baskets = new Dictionary<int, int>();
        var start = 0;
        var maxWindowLength = 0;

        for (int i = 0; i < fruits.Length; i++){
            var fruitType = fruits[i];
            if (baskets.ContainsKey(fruitType)) baskets[fruitType]++;
            else baskets[fruitType] = 1;

            while (baskets.Count > 2){
                var letFruit = fruits[start];
                baskets[letFruit]--;
                if (baskets[letFruit] == 0) baskets.Remove(letFruit);
                start++;
            }

            maxWindowLength = Math.Max(maxWindowLength, i - start + 1);
        }

        return maxWindowLength;
    }
}