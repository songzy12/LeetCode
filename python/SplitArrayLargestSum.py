# Given an array which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays. 
# Write an algorithm to minimize the largest sum among these m subarrays. 

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = max(nums)
        r = sum(nums)
    
        def check(candidate):
            t = m
            i = 0
            while t:
                temp = 0
                while i < len(nums) and temp + nums[i] <= candidate:
                    temp += nums[i]
                    i += 1
                t -= 1
            
            return i == len(nums) 
        
        if check(l):
            return l
            
        while l < r:
            m_ = (l + r) / 2  # not to mix with parameter m
            if not check(m_):
                l = m_ + 1
            else:
                r = m_
        return l
        
nums = [7,2,5,10,8]
m = 2
print Solution().splitArray(nums, m)

# divide as equal as possible
# no idea

# Given a result, it is easy to test whether it is valid or not.
# The max of the result is the sum of the input nums.
# The min of the result is the max num of the input nums