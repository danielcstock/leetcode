class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        baskets = {}
        start = 0
        maxWindowLength = 0
        
        for end in range(len(fruits)):
            fruit = fruits[end]
            baskets[fruit] = baskets.get(fruit, 0) + 1

            while len(baskets) > 2:
                letFruit = fruits[start]
                baskets[letFruit] -= 1
                if baskets[letFruit] == 0:
                    del baskets[letFruit]
                start +=1
            
            maxWindowLength = max(maxWindowLength, end - start + 1)

        return maxWindowLength    