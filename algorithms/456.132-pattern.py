class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = - 1 << 32
        st = []
        for num in nums[::-1]:
            if num < s3:
                return True
            else:
                # for now, num >= s3
                while st and num > st[-1]:
                    s3 = st.pop(-1)
                # each time, s3 is largest possible
                st += num,
        return False

nums = [-1,3,2,0]
print Solution().find132pattern(nums)
