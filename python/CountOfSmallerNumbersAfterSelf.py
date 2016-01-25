class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = [0] * len(nums)
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]: # sort backward
                    if not right or left and left[-1][1] > right[-1][1]:
                        # left[-1] is largest in remained numbers
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        sort(list(enumerate(nums))) # to denote origin position
        return smaller
        
nums = [5, 2, 6, 1]
print Solution().countSmaller(nums)
