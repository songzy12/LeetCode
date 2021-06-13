
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sums = [0 for i in range(len(nums)+1)]
        for i in range(len(nums)):
            sums[i+1] = sums[i]+nums[i]
        
        for j in range(3, len(nums)-2):
            m = {} 
            for i in range(j-1):
                sum1 = sums[i]
                sum2 = sums[j] - sums[i+1]
                if sum1 == sum2:
                    m[sum1] = True
            for k in range(j+2,len(nums)-1):
                sum1 = sums[k] - sums[j+1]
                sum2 = sums[len(nums)] - sums[k+1]
                if sum1 == sum2 and sum1 in m:
                    return True
        return False

        
    
if __name__ == '__main__':
    nums = [-1,0,0,-1,0,-1,0,-1]
    print Solution().splitArray(nums)

# enumerate i
# for each valid i, find valiad j
# for each valid j, find valid k
# for each valid k, find valid n
# check whether n == len(nums)
# TLE

# enumerate j
# find all the possible valid i, store the sum in a map
# for each valid k, check whether it appears in the left
