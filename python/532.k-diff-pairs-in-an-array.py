class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        from collections import Counter
        c = Counter(nums)
        if not k:
            return sum([1 for t,n in c.items() if n>1])
        else:
            ans = 0
            for t,v in c.items():
                ans += 1 if c[t+k] else 0
            return ans

if __name__ == '__main__':
    for nums, k in [([3,1,4,1,5],2),([1,2,3,4,5], 1), ([1,3,1,5,4],0)]:
        print Solution().findPairs(nums, k)
