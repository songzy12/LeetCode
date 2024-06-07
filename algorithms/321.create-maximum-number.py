class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        def prep(nums, k):
            # pick k num from nums to form max number
            drop = len(nums) - k
            out = []
            for num in nums:
                while drop and out and out[-1] < num:
                    out.pop()
                    drop -= 1
                out.append(num)
            return out[:k]

        def merge(a, b):
            # merge two nums to form max number
            return [max(a, b).pop(0) for _ in a+b]

        return max(merge(prep(nums1, i), prep(nums2, k-i))
                   for i in range(k+1)
                   if i <= len(nums1) and k-i <= len(nums2))


nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
print Solution().maxNumber(nums1, nums2, k)

nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
print Solution().maxNumber(nums1, nums2, k)

nums1 = [3, 9]
nums2 = [8, 9]
k = 3
print Solution().maxNumber(nums1, nums2, k)
