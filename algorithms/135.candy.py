class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        if not ratings:
            return 0
        num = len(ratings)
        result = [1]*num
        for i in range(1,num):
            if ratings[i]>ratings[i-1]:
                result[i] = result[i-1] + 1
        for i in range(num-2, -1, -1):
            if ratings[i]>ratings[i+1] and result[i]<=result[i+1]:
                result[i] = result[i+1] + 1
        return sum(result)

import random
ratings = [random.randint(0,5) for i in range(5)]
print(ratings, Solution().candy(ratings))
