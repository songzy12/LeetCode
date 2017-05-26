class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        max_m = {}
        min_m = {}
        def max_dp(i, j):
            # return the max value
            # with the sequence to get that value
            if i == j:
                return nums[i], [nums[i]]
            if (i, j) in max_m:
                return max_m[(i, j)]
            temp_result = 0
            temp_sequence = []
            for k in range(i, j):
                ma, mas = max_dp(i, k)
                mi, mis = min_dp(k+1, j)
                if ma * 1.0 / mi > temp_result:
                    temp_result = ma * 1.0 / mi
                    temp_sequence = [mas, mis]
            max_m[(i, j)] = temp_result, temp_sequence
            return max_m[(i, j)]

        def min_dp(i, j):
            if i == j:
                return nums[i], [nums[i]]
            if (i, j) in min_m:
                return min_m[(i, j)]
            temp_result = 1000**5
            temp_sequence = []
            for k in range(i, j):
                mi, mis = min_dp(i, k)
                ma, mas = max_dp(k+1, j)
                if mi * 1.0 / ma < temp_result:
                    temp_result = mi * 1.0 / ma
                    temp_sequence = [mis, mas]
            min_m[(i, j)] = temp_result, temp_sequence
            return min_m[(i, j)]
        ma, mas = max_dp(0, len(nums)-1)

        def convert(s):
            if len(s) == 1:
                return str(s[0])
            if len(s[-1]) == 1:
                return convert(s[0]) + "/" + convert(s[-1])
            return convert(s[0]) + "/" + "(" + convert(s[-1]) + ")"
        return convert(mas)
            
nums = [1000,100,10,2]
print Solution().optimalDivision(nums)

# use two dp: max_dp, min_dp
# then discuss where the last division happens
