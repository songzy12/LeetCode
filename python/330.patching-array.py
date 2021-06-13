class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        # if we have patched [1..n-1], adding n will patch [1..2*n-1]
        current = 1 # next number we need
        count = 0
        for i in range(len(nums)):
            while current < nums[i]:
                if current > n:
                    break
                count += 1
                current += current # we patch current
            if current > n:
                break
            current += nums[i]
        while current <= n:
            count += 1
            current += current
        return count
            
nums = [1,7,21,31,34,37,40,43,49,87,90,92,93,98,99]
n = 12
print Solution().minPatches(nums, n)
        
