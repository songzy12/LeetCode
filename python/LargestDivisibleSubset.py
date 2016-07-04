class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        # T[i]: when nums[i] is largest of subset, the largest result
        # m: the value of the largest result
        # mi: the index of the largest element with the largest result
        # parent[i]: parent of i in the result array
        T = [1 for i in range(len(nums))]
        mi = m = 0
        parent = [-1 for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and T[i] < T[j] + 1:
                    T[i] = T[j] + 1
                    parent[i] = j
                    if T[i] > m:
                        m = T[i]
                        mi = i

        res = []
        while mi != -1:
            res += nums[mi],
            mi = parent[mi]
        return res
      
nums = [1]  
print Solution().largestDivisibleSubset(nums)
